from typing import Dict, Tuple
from bpy.types import Armature, Object
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.blender_rigging_helper import BlenderRiggingHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.blender_armature_constructor import BlenderArmatureConstructor
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_edit_mode_arm_model_fact import BlenderEditModeArmatureModelFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class BlenderSkinnedObjectsWithArmatureFactory:
    @classmethod
    def _parent_blender_object_to_armature_with_bones_vertex_groups(
        cls,
        armature_obj: Object,
        subobject: Subobject,
        blender_mesh_obj: Object
    ):
        BlenderRiggingHelper.parent_blender_object_to_armature_with_bones_vertex_groups(
            armature_obj=armature_obj,
            bones_vertex_groups=subobject.geometric_object.bone_weights,
            blender_mesh_obj=blender_mesh_obj
        )

        raise NotImplementedError


    @classmethod
    def build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
        cls,
        subobjects: Dict[int, Subobject],
        subobjects_mesh_objects: Dict[int, Object],
        armature_bind_pose_model: TreeHierarchy,
        armature_name: str) -> Tuple[Armature, Object]:

        blender_edit_mode_armature_model_factory = BlenderEditModeArmatureModelFactory()
        blender_armature_constructor = BlenderArmatureConstructor()

        blender_edit_mode_armature_model = \
            blender_edit_mode_armature_model_factory.get_blender_edit_mode_armature_model(
                subobjects=subobjects
            )  # type: TreeHierarchy

        blender_armature_data_block, blender_armature_obj = blender_armature_constructor.build_armature(
            blender_edit_mode_armature_model=blender_edit_mode_armature_model,
            name=armature_name
        )

        for subobject in subobjects.values():
            cls._parent_blender_object_to_armature_with_bones_vertex_groups(
                armature_obj=blender_armature_obj,
                subobject=subobject,
                blender_mesh_obj=subobjects_mesh_objects[subobject.object_number]
            )

        raise NotImplementedError
