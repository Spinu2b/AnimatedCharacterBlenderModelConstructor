from typing import Dict
from acbmc.model.animated_character.model.animation_clips import AnimationClips
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.uni_ani_clip_arm_tree_hier_with_def_sets_fetch import \
 UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.uni_art_conv_def_set_arm_bind_pos_build \
 import UnifiedArtistConvenientDeformSetsArmatureBindPoseBuilder
from acbmc.model.blender.model.armature_bind_pose_model import ArmatureBindPoseModel
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class ChannelsWithSubobjectsDeformSetsConvenientArtistGlobalRootedArmatureBindPoseFetcher:
    def derive_armature_bind_pose_model(
        self,
        animation_clips: AnimationClips,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: ChannelHierarchies,
        subobjects_channels_associations: SubobjectsChannelsAssociations) -> ArmatureBindPoseModel:
        
        result_builder = UnifiedArtistConvenientDeformSetsArmatureBindPoseBuilder()
        armature_tree_hierarchies_fetcher = UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher()
        for animation_clip_id in animation_clips.animation_clips:
            animation_clip_obj = animation_clips.animation_clips[animation_clip_id]  # type: AnimationClip
            for armature_tree_hierarchy_with_deform_sets_in_animation_clip in \
                armature_tree_hierarchies_fetcher.iterate_armature_hierarchies_with_deform_sets_for_animation_clip(
                    animation_clip=animation_clip_obj, subobjects_dict=subobjects_dict,
                    channel_hierarchies=channel_hierarchies, subobjects_channels_associations=subobjects_channels_associations):
                result_builder.consider_armature_hierarchy_with_deform_sets(armature_tree_hierarchy_with_deform_sets_in_animation_clip)

        return result_builder.build()
