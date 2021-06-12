from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.building.bone_nodes.bone_nodes_factory import BoneNodesFactory
from typing import Dict, List
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_arm_model_fact import BlenderArmatureModelFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model \
    .channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class ChannelIdsForArmatureFetcher:
    @classmethod
    def get_unique_channel_ids_for_channel_hierarchies(
        cls,
        channel_hierarchies: Dict[str, ChannelHierarchy]) -> List[int]:
        raise NotImplementedError


class BlenderBindPoseArmatureModelWithChannelsFactory(BlenderArmatureModelFactory):
    def get_blender_armature_model(self, data: any) -> TreeHierarchy:
        subobjects = data[0]  # type: Dict[int, Subobject]
        channel_hierarchies = data[1]  # type: Dict[str, ChannelHierarchy]

        base_model = super().get_blender_armature_model(subobjects)

        channel_ids = ChannelIdsForArmatureFetcher.get_unique_channel_ids_for_channel_hierarchies(channel_hierarchies)

        raise NotImplementedError

    def __init__(self, bone_nodes_factory: BoneNodesFactory):
        super().__init__(bone_nodes_factory)
