from typing import Dict
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .subobjects.subobjects_morph_usage_helper import SubobjectsMorphUsageHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_bind_pose_arm_model_fact import BlenderBindPoseArmatureModelFactory
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.anim_char_with_one_glob_root_arm_const import \
 AnimatedCharacterWithOneGlobalRootedArmatureConstructor
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.uni_glob_root_arm_bind_pose_model_fetch import \
 UnifiedGlobalRootedArmatureBindPoseModelFetcher
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.blender_operations.model_build.animated_character_constructor import AnimatedCharacterConstructor


class MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor(AnimatedCharacterConstructor):
    def construct_animated_character(self, animated_character_description: AnimatedCharacterDescription):
        # This bad boy here has to serve us the bind pose model that should be relatively
        #  convenient for animators/3d artists to work with
        
        #one_unified_global_rooted_armature_bind_pose_model = \
        #    UnifiedGlobalRootedArmatureBindPoseModelFetcher(). \
        #        get_unified_global_rooted_armature_bind_pose_model(animated_character_description)

        blender_bind_pose_armature_model_factory = BlenderBindPoseArmatureModelFactory()

        core_subobjects = SubobjectsMorphUsageHelper \
            .get_core_actual_subobjects_considering_morph_data(
                subobjects=animated_character_description.subobjects_library.subobjects,
                animation_clips=animated_character_description.animation_clips) # type: Dict[int, Subobject] 

        bind_pose_armature_bone_transformations_model_from_subobjects_governing_bones = \
            blender_bind_pose_armature_model_factory.get_blender_armature_model(core_subobjects)

        # The known and verified way by me to export to FBX using builting FBX export is to have one global armature with 
        # one root bone, it supports dynamic Child-Of bone constraint so thats fine, we can alter bones' parenting during animations
        # To have objects disappearing and appearing in particular keyframes we can use verified way of setting their scale
        # to near zero

        # To not have glitches with appearing/disappearing objects one should use keyframes that are 1 frame apart with
        # no linear interpolation between them (i.e 0.0 -> 1.0 or jump between any two values using keyframes 1 frame apart)
        # but that might not be well supported by Blender fbx export, so there are flags to alter that behaviour
        # for the sake of somewhat working animations

        # One might need to write custom FBX export for Blender dedicated for this using Autodesk FBX SDK
        # From what I understand the BlendShapes are not supported at all, but thats necessity for us, so 
        # we will eventually end up with writing dedicated FBX export anyway...
        # we don't strive for dirty solutions, because we want files (models) to not have the weight bigger than neccessary (performance)

        # Plus writing custom FBX export will allow us to alter the model and armature in any way when it already has some animations (actions)
        # Builting Blender FBX export breaks everything in this matter
        # Probably the way data blocks are being aggregated when each new operation on the model is being done and then FBX export logic is
        #  confused by that
        # We will need to deal with it anyway ourselves, would be cool to have such capability to alter the model freely when it has animations already

        AnimatedCharacterWithOneGlobalRootedArmatureConstructor().construct_using(
            #armature_bind_pose_model=one_unified_global_rooted_armature_bind_pose_model,
            armature_bind_pose_model=bind_pose_armature_bone_transformations_model_from_subobjects_governing_bones,
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
