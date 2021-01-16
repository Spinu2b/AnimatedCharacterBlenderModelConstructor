from typing import Dict
from bpy.types import Action, Object
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.mesh_normalizer import MeshNormalizer
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.visual_data_holder import VisualDataHolder
from acbmc.model.animated_character.model.animation_clips import AnimationClips
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.blender_skin_obj_with_arm_fact import BlenderSkinnedObjectsWithArmatureFactory
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

        # first let's just animate armature's bones skipping morphs
        # this will be incremental approach for implementation

        animation_clips_dict = animation_clips.animation_clips  # type: Dict[int, AnimationClip]

        blender_editor_manipulator = BlenderEditorManipulator()
        blender_editor_manipulator.enter_pose_mode()

        blender_editor_manipulator.set_context_area_ui_type_to_dopesheet()
        blender_editor_manipulator.set_context_space_data_ui_mode_to_action()

        for animation_clip_id in animation_clips_dict:
            animation_clip_name = UnifiedArmatureWithDeformSetsBonesNamingHelper \
                .get_animation_clip_name_for(animation_clip_id)  # type: str
            action = blender_editor_manipulator.enter_animation_clip(name=animation_clip_name)  # type: Action
            blender_editor_manipulator.set_armature_active_action(blender_armature_obj, action)
            animation_clip_obj = animation_clips_dict[animation_clip_id]

            # Here - to implement iterating though animation clip's whole frames and setting bones' actual keyframes
            # here and there

            for pose_armature_hierarchy, animation_frame_number_for_keyframe \
                in AnimationFramesIteratingHelper \
                    .iterate_appropriate_pose_armature_hierarchies_for_keyframes_setting(
                        animation_clip=animation_clip_obj,
                        armature_bind_pose_hierarchy=armature_bind_pose_model 
                    ):

                    blender_editor_manipulator.enter_frame_number(frame_number=animation_frame_number_for_keyframe)
                    self._set_pose_in_current_animation_frame(pose_armature_hierarchy)
            
            raise NotImplementedError
            #animation_frames = animation_clips_dict[animation_clip_id].get_frames_count()  # type: int

            #for animation_frame_number in animation_frames:

 
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

        visual_data_holder = VisualDataHolder()
        blender_mesh_objects = dict()  # type: Dict[int, Object]
        for subobject_number in core_subobjects:   
            subobject = core_subobjects[subobject_number]  # type: Subobject
            blender_mesh_obj = BlenderObjectWithMeshGeometryFactory \
                .create_from_subobject_desc(
                    visual_data=visual_data,
                    visual_data_holder=visual_data_holder,
                    subobject_number=subobject_number,
                    subobject=subobject)  # type: Object
            blender_mesh_objects[subobject_number] = blender_mesh_obj

        blender_armature_data_block, blender_armature_obj = \
            BlenderSkinnedObjectsWithArmatureFactory.build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
                armature_bind_pose_model=armature_bind_pose_model,
                subobjects=core_subobjects,
                subobjects_mesh_objects=blender_mesh_objects,
                armature_name=self.ARMATURE_NAME
            )

        for blender_mesh_obj in blender_mesh_objects.values():
            MeshNormalizer.normalize_mesh(blender_mesh_obj)

        self._animate_armature_with_animation_clips_creating_actions_in_action_editor(
            animation_clips=animated_character_description.animation_clips,
            armature_bind_pose_model=armature_bind_pose_model,
            blender_armature_obj=blender_armature_obj
        )

        raise NotImplementedError
