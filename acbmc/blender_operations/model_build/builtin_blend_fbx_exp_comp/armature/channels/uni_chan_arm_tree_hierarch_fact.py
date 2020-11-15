from typing import Dict, Iterator, List, Optional, Set, Tuple
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.model.tree_hierarchy_builder import TreeHierarchyBuilder
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.blender.model.armature.armature_tree_hierarchy import ArmatureTreeHierarchy, ArmatureTreeHierarchyNode


class ChannelsSetsParentingHelper:
    @classmethod
    def _get_children_list_for_channel_id(cls, channel_id: int, channels_parenting: Dict[int, int]) -> List[int]:
        return [x for x in channels_parenting if channels_parenting[x] == channel_id]

    @classmethod
    def _traverse(cls, parent_root_channel_id: Optional[int],
         root_channels: List[int], channels_set: Set[int], channels_parenting: Dict[int, int]) \
         -> Iterator[Tuple[int, Optional[int]]]:
        for root_channel_id in root_channels:
            yield root_channel_id, parent_root_channel_id
            root_channel_children_list = cls._get_children_list_for_channel_id(root_channel_id, channels_parenting)
            yield from cls._traverse(
                parent_root_channel_id=root_channel_id,
                root_channels=root_channel_children_list, channels_set=channels_set, channels_parenting=channels_parenting)
        
    @classmethod
    def iterate_channels_in_order_of_constructing_the_tree(cls, 
        channels_set: Set[int], channels_parenting: Dict[int, int]) -> Iterator[Tuple[int, Optional[int]]]:

        root_channels = [channel_id for channel_id in channels_set if channel_id not in channels_parenting]  # type: List[int]
        yield from cls._traverse(
            parent_root_channel_id=None, root_channels=root_channels,
            channels_set=channels_set, channels_parenting=channels_parenting)


class UnifiedChannelsArmatureTreeHierarchyFactory:
    @staticmethod
    def construct_pure_channels_armature_tree_hierarchy(
        channels_set: Set[int],
        channels_parenting: Dict[int, int],
        channel_transforms: Dict[int, ChannelTransform]
    ) -> ArmatureTreeHierarchy:
        tree_hierarchy_builder = TreeHierarchyBuilder()
        tree_hierarchy_builder.set_tree_hierarchy_class(ArmatureTreeHierarchy)

        for channel_id, parent_channel_id in ChannelsSetsParentingHelper \
            .iterate_channels_in_order_of_constructing_the_tree(channels_set, channels_parenting):
            tree_hierarchy_builder \
                .add_node(
                    parent_key= \
                        UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_channel_id(parent_channel_id)
                        if parent_channel_id is not None else None,
                    node=ArmatureTreeHierarchyNode.from_channel_transform(
                        bone_name=
                            UnifiedArmatureWithDeformSetsBonesNamingHelper \
                                .get_bone_name_for_channel_id(channel_id=channel_id),
                        channel_transform=channel_transforms[channel_id]),
                    key=UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_channel_id(channel_id))

        return tree_hierarchy_builder.build()
