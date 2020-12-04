from acbmc.model.animated_character.model.animation_clips import AnimationClips
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.constructing.blender_skin_obj_with_arm_fact import BlenderSkinnedObjectsWithArmatureFactory
from typing import Dict
from bpy.types import Object
from acbmc.blender_operations \
    .model_build.builtin_blend_fbx_exp_comp.subobjects.blender_object_with_mesh_geo_fact import BlenderObjectWithMeshGeometryFactory
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.subobjects_library_desc.visual_data import VisualData
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.subobjects_morph_usage_helper import SubobjectsMorphUsageHelper
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription


class AnimatedCharacterWithOneGlobalRootedArmatureConstructor:
    ARMATURE_NAME = "CHARACTER_ARMATURE"

    def _animate_armature_with_animation_clips_creating_actions_in_action_editor(
        self,
        animation_clips: AnimationClips, 
        armature_bind_pose_model: TreeHierarchy, 
        blender_armature_obj: Object):
        raise NotImplementedError

    def construct_using(
        self,
        armature_bind_pose_model: TreeHierarchy,
        animated_character_description: AnimatedCharacterDescription, 
        allow_actual_zero_linear_interpolation_on_the_timeline: bool,
        allow_objects_having_actual_zero_scale: bool,
        parent_every_bone_to_root_using_regular_constant_child_parent_constraint: bool):

        subobjects_dict = animated_character_description.subobjects_library.subobjects # type: Dict[int, Subobject]
        visual_data = animated_character_description.subobjects_library.visual_data  # type: VisualData
        core_subobjects = SubobjectsMorphUsageHelper \
            .get_core_actual_subobjects_considering_morph_data(
                subobjects=subobjects_dict, animation_clips=animated_character_description.animation_clips) # type: Dict[int, Subobject] 

        blender_mesh_objects = dict()  # type: Dict[int, Object]
        for subobject_number in core_subobjects:   
            subobject = core_subobjects[subobject_number]  # type: Subobject
            blender_mesh_obj = BlenderObjectWithMeshGeometryFactory \
                .create_from_subobject_desc(visual_data, subobject_number, subobject)  # type: Object
            blender_mesh_objects[subobject_number] = blender_mesh_obj

        blender_armature_data_block, blender_armature_obj = \
            BlenderSkinnedObjectsWithArmatureFactory.build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
                armature_bind_pose_model=armature_bind_pose_model,
                subobjects=core_subobjects,
                subobjects_mesh_objects=blender_mesh_objects,
                name=self.ARMATURE_NAME
            )

        self._animate_armature_with_animation_clips_creating_actions_in_action_editor(
            animation_clips=animated_character_description.animation_clips,
            armature_bind_pose_model=armature_bind_pose_model,
            blender_armature_obj=blender_armature_obj
        )

        raise NotImplementedError
