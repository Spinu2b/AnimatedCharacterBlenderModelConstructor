from acbmc.util.tree_iteration_helper import TreeIterationHelper
from typing import Dict, Iterator, List, Optional, Set, Tuple
from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.model.tree_hierarchy_builder import TreeHierarchyBuilder
from acbmc.model.blender.model.armature.armature_tree_hierarchy import ArmatureTreeHierarchy


class ChannelsSetsParentingHelper:
    @classmethod
    def iterate_channels_in_order_of_constructing_the_tree(cls, 
        channels_set: Set[int], channels_parenting: Dict[int, int]) -> Iterator[Tuple[int, Optional[int]]]:

        result = [(x, None) for x in channels_set] + [(x, channels_parenting[x]) for x in channels_parenting]  # type: List[Tuple[int, Optional[int]]]
        yield from TreeIterationHelper.iterate_sequence_in_order_of_tree_building(
            collection=result,
            parent_key_getter=lambda element: element[1],
            node_key_getter=lambda element: element[0]
        )


class UnifiedChannelsArmatureTreeHierarchyFactory:
    @staticmethod
    def construct_pure_channels_armature_tree_hierarchy(
        channels_set: Set[int],
        channels_parenting: Dict[int, int],
        channel_transforms: Dict[int, TransformNode]
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
                    node=BoneAbsoluteTransformNode.from_transform_node(
                        bone_name=
                            UnifiedArmatureWithDeformSetsBonesNamingHelper \
                                .get_bone_name_for_channel_id(channel_id=channel_id),
                        transform_node=channel_transforms[channel_id]),
                    key=UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_channel_id(channel_id))

        return tree_hierarchy_builder.build()
