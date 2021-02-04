from typing import Dict, Iterator
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.model.transform_node import TransformNode
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class ChannelKeyframesHelper:
    @classmethod
    def has_actual_keyframes_in_frame(
        cls,
        frame_number: int,
        channel_keyframes: Dict[int, Dict[int, TransformNode]]) -> bool:
        
        raise NotImplementedError

    @classmethod
    def iterate_keyframe_channel_ids_for_frame(
        cls,
        frame_number: int,
        channel_keyframes: Dict[int, Dict[int, TransformNode]]
    ) -> Iterator[int]:

        for channel_id in channel_keyframes:
            if frame_number in channel_keyframes[channel_id]:
                yield channel_id


class UnifiedChannelArmatureTreeHierarchyKeyframesFiller:
    @classmethod
    def fill_tree_hierarchy_with_channel_keyframes_flags(
        cls,
        armature_tree_hierarchy: TreeHierarchy,
        channel_keyframes: Dict[int, Dict[int, TransformNode]],
        frame_number: int
    ):
        for keyframed_channel_id_in_given_animation_frame in \
            ChannelKeyframesHelper.iterate_keyframe_channel_ids_for_frame(frame_number, channel_keyframes):

            respective_compliant_bone_name_to_keyframe = \
                UnifiedArmatureWithDeformSetsBonesNamingHelper \
                    .get_bone_name_for_channel_id(keyframed_channel_id_in_given_animation_frame)
            respective_bone_node_to_keyframe = armature_tree_hierarchy.get_node_reference(respective_compliant_bone_name_to_keyframe)
            respective_bone_node_to_keyframe.node.is_keyframe = True
