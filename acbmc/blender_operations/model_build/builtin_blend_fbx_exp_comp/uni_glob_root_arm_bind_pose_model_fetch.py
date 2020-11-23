from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.chan_with_subobj_def_sets_conv_art_glob_root_arm_bind_pos_fetch import \
 ChannelsWithSubobjectsDeformSetsConvenientArtistGlobalRootedArmatureBindPoseFetcher
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription


class UnifiedGlobalRootedArmatureBindPoseModelFetcher:
    def get_unified_global_rooted_armature_bind_pose_model(self,
     animated_character_description: AnimatedCharacterDescription) -> TreeHierarchy:
     armature_bind_pose_model = \
        ChannelsWithSubobjectsDeformSetsConvenientArtistGlobalRootedArmatureBindPoseFetcher() \
            .derive_armature_bind_pose_model(
                animation_clips=animated_character_description.animation_clips,
                subobjects_dict=animated_character_description.subobjects_library.subobjects,
                channel_hierarchies=animated_character_description.channel_hierarchies,
                subobjects_channels_associations=animated_character_description.subobjects_channels_associations
            )
     return armature_bind_pose_model
