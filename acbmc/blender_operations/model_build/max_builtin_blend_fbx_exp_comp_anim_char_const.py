from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.building.bone_nodes.normal_bone_nodes_factory import NormalBoneNodesFactory
from typing import Dict
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building \
    .blender_bind_pos_arm_model_with_chan_fact import BlenderBindPoseArmatureModelWithChannelsFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .subobjects.subobjects_morph_usage_helper import SubobjectsMorphUsageHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.anim_char_with_one_glob_root_arm_const import \
 AnimatedCharacterWithOneGlobalRootedArmatureConstructor
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.blender_operations.model_build.animated_character_constructor import AnimatedCharacterConstructor


class MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor(AnimatedCharacterConstructor):
    def construct_animated_character(self, animated_character_description: AnimatedCharacterDescription):
        blender_bind_pose_armature_model_factory = BlenderBindPoseArmatureModelWithChannelsFactory(NormalBoneNodesFactory())

        core_subobjects = SubobjectsMorphUsageHelper \
            .get_core_actual_subobjects_considering_morph_data(
                subobjects=animated_character_description.subobjects_library.subobjects,
                animation_clips=animated_character_description.animation_clips) # type: Dict[int, Subobject] 

        # bind_pose_armature_bone_transformations_model_from_subobjects_governing_bones = \
        #    blender_bind_pose_armature_model_factory.get_blender_armature_model(core_subobjects)

        bind_pose_armature_model_with_channel_bones = \
            blender_bind_pose_armature_model_factory.get_blender_armature_model(
                [core_subobjects, animated_character_description.channel_hierarchies.channel_hierarchies]
            )

        AnimatedCharacterWithOneGlobalRootedArmatureConstructor().construct_using(
            #armature_bind_pose_model=one_unified_global_rooted_armature_bind_pose_model,
            armature_bind_pose_model=bind_pose_armature_model_with_channel_bones,
            animated_character_description=animated_character_description,
            # setting below flag to False WILL introduce glitches in animations with appearing/disappearing objects 
            # but will work with builtin FBX Blender export
            allow_actual_zero_linear_interpolation_on_the_timeline=True,
            # setting below flag to False will set objects to have near-zero scale (will work with builtin FBX Blender export)
            allow_objects_having_actual_zero_scale=True,
            # setting this to False will use dynamic Child-Of constraint for each bones' pair, even the ones that are not supposed to change during animations
            # (i.e. parenting each otherwise-root-bone to global root bone of whole armature, you get the idea,
            #  this must simply work with FBX Blender export in any case!)
            # Setting this to True on the other hand will parent every bone in the armature to root bone, and this will be combined
            # with dynamic Child-Of constraint, which might give strange results (not checked experimentally yet)

            # This one might actually cause some unsolvable problems, so this might eventually require writing custom FBX export
            parent_every_bone_to_root_using_regular_constant_child_parent_constraint=False
        )    
