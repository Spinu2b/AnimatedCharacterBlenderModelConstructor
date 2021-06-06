from typing import Dict, Tuple
from bpy.types import Armature, Object
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.armature.blender_armature_constructor import BlenderArmatureConstructor
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.blender_rigging_helper import BlenderRiggingHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_edit_mode_arm_model_fact import BlenderEditModeArmatureModelFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class ObjectBoneParentingBoneWeightsHelper:
    @classmethod
    def get_mock_bone_weights_for_bone_object_parenting(cls, subobject: Subobject) -> Dict[str, Dict[int, float]]:
        result = dict()  # type: Dict[str, Dict[int, float]]
        result[
            UnifiedArmatureWithDeformSetsBonesNamingHelper
                .get_mock_bone_name_for_object_parenting(subobject.object_number)] = \
                     {key:1.0 for key, _ in enumerate(subobject.geometric_object.vertices)}
        return result

    @classmethod
    def get_bone_weights_data_prepared_for_skinning(cls, subobject: Subobject) -> Dict[str, Dict[int, float]]:
        result = dict()  # type: Dict[str, Dict[int, float]]
        for bone_index in subobject.geometric_object.bone_weights:
            bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper \
                .get_bone_name_for(bone_in_subobject_index=bone_index, subobject_number=subobject.object_number)
            result[bone_name] = {key:value for key, value in subobject.geometric_object.bone_weights[bone_index].items()}
        return result


class BlenderSkinnedObjectsWithArmatureFactory:
    @classmethod
    def _parent_blender_object_to_armature_with_bones_vertex_groups(
        cls,
        armature_obj: Object,
        subobject: Subobject,
        blender_mesh_obj: Object
    ):

        if subobject.contains_actual_bones():
            BlenderRiggingHelper.parent_blender_object_to_armature_with_bones_vertex_groups(
                armature_obj=armature_obj,
                bones_vertex_groups=ObjectBoneParentingBoneWeightsHelper \
                    .get_bone_weights_data_prepared_for_skinning(subobject),
                blender_mesh_obj=blender_mesh_obj
            )
        else:
            BlenderRiggingHelper.parent_blender_object_to_armature_with_bones_vertex_groups(
                armature_obj=armature_obj,
                bones_vertex_groups=ObjectBoneParentingBoneWeightsHelper \
                    .get_mock_bone_weights_for_bone_object_parenting(subobject),
                blender_mesh_obj=blender_mesh_obj
            )

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
            blender_edit_mode_armature_model_factory.get_blender_armature_model(subobjects)  # type: TreeHierarchy

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

        return blender_armature_data_block, blender_armature_obj

        # raise NotImplementedError
