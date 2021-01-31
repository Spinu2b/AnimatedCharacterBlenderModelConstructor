from typing import Dict, Iterator, List, Tuple
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .animations.flat_arm_hierarchy_helper import FlattenedArmatureHierarchyHelper
from acbmc.model.animated_character.model \
    .subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_ani_clip_arm_tree_hier_with_def_sets_fetch import ChannelKeyframesHelper, \
     UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class KeyframeDataFillingPoseHierarchyTransformation:
    @classmethod
    def to_keyframed_pose_hierarchy_transformation(
        cls,
        tree_hierarchy: TreeHierarchy,
        channel_keyframes: Dict[int, Dict[int, TransformNode]],
        frame_number: int,
        channel_hierarchy: ChannelHierarchy,
        channels_for_subobjects_association: SubobjectsChannelsAssociation) -> TreeHierarchy:

        for keyframe_channel_id_in_frame in ChannelKeyframesHelper \
            .iterate_keyframe_channel_ids_for_frame(frame_number, channel_keyframes):

            # we operate on flat armature hierarchy that considers only bones related to deform sets, without actual channel bones
            result_keyframed_bones_name = FlattenedArmatureHierarchyHelper.get_bone_names_qualified_for_keyframing_in_flattened_hierarchy(
                keyframe_channel_id_in_frame, channel_hierarchy, channels_for_subobjects_association
            )

            for keyframed_bone_name in result_keyframed_bones_name:
                bone_node = next(x for x in tree_hierarchy.iterate_nodes() if x.node.bone_name == keyframed_bone_name)
                bone_node.node.is_keyframe = True

        return tree_hierarchy


class AnimationFramesIteratingHelper:
    @classmethod
    def iterate_appropriate_pose_armature_hierarchies_for_keyframes_setting(
        cls,
        animation_clip: AnimationClip,
        armature_bind_pose_hierarchy: TreeHierarchy,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: ChannelHierarchies,
        subobjects_channels_associations: SubobjectsChannelsAssociations) -> Iterator[Tuple[int, TreeHierarchy]]:

        pose_hierarchies_with_keyframe_data = []  # type: List[Tuple[int, TreeHierarchy]]

        armature_tree_hierarchies_fetcher = UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher()
        for frame_number, armature_tree_hierarchy_with_deform_sets_in_animation_clip in \
                armature_tree_hierarchies_fetcher.iterate_armature_hierarchies_with_deform_sets_for_animation_clip(
                    animation_clip=animation_clip, subobjects_dict=subobjects_dict,
                    channel_hierarchies=channel_hierarchies, subobjects_channels_associations=subobjects_channels_associations,
                    new_tree_hierarchy_for_each_keyframes_set_change=True,
                    result_tree_hierarchy_transformation= \
                        KeyframeDataFillingPoseHierarchyTransformation.to_keyframed_pose_hierarchy_transformation):
            
            raise NotImplementedError
        
        raise NotImplementedError
