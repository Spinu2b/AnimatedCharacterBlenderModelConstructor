from typing import Dict, Iterator, List, Set
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.bone_nodes_factory import BoneNodesFactory
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_arm_model_fact import BlenderArmatureModelFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model \
    .channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class ChannelIdsForArmatureFetcher:
    @classmethod
    def _iterate_channels_parenting_dicts(cls, channel_hierarchies: Dict[str, ChannelHierarchy]) -> Iterator[Dict[int, int]]:
        for channel_hierarchy in channel_hierarchies.values():
            yield channel_hierarchy.channel_hierarchy.parenting

    @classmethod
    def _get_unique_channels_id_from_parenting_dict(cls, channels_parenting_dict: Dict[int, int]) -> Set[int]:
        result = set()
        for parenting_pair in channels_parenting_dict.items():
            result.add(parenting_pair[0])
            result.add(parenting_pair[1])
        return result

    @classmethod
    def get_unique_channel_ids_for_channel_hierarchies(
        cls,
        channel_hierarchies: Dict[str, ChannelHierarchy]) -> List[int]:
        result = set()        
        for channels_parenting_dict in cls._iterate_channels_parenting_dicts(channel_hierarchies):
            unique_channels_ids = cls._get_unique_channels_id_from_parenting_dict(channels_parenting_dict)
            result = result.union(unique_channels_ids)

        return list(result)

class BlenderBindPoseArmatureModelWithChannelsFactory(BlenderArmatureModelFactory):
    def get_blender_armature_model(self, data: any) -> TreeHierarchy:
        subobjects = data[0]  # type: Dict[int, Subobject]
        channel_hierarchies = data[1]  # type: Dict[str, ChannelHierarchy]

        base_model = super().get_blender_armature_model(subobjects)

        channel_ids = ChannelIdsForArmatureFetcher.get_unique_channel_ids_for_channel_hierarchies(channel_hierarchies)
        for chan_id in channel_ids:
            channel_bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_channel_id(chan_id)
            base_model.add_node(
                parent_key=None,
                node_key=channel_bone_name,
                node=self.bone_nodes_factory.get_home_transformed_bone_node(channel_bone_name)
            )

        return base_model

    def __init__(self, bone_nodes_factory: BoneNodesFactory):
        super().__init__(bone_nodes_factory)
