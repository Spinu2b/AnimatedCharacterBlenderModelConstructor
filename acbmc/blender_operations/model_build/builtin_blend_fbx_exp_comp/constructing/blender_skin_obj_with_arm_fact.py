from typing import Dict, Tuple
from bpy.types import Armature, Object
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class BlenderSkinnedObjectsWithArmatureFactory:
    @classmethod
    def build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
        cls,
        subobjects: Dict[int, Subobject],
        subobjects_mesh_objects: Dict[int, Object],
        armature_bind_pose_model: TreeHierarchy,
        armature_name: str) -> Tuple[Armature, Object]:

        blender_edit_mode_armature_model_factory = BlenderEditModeArmatureModelFactory()
        blender_rigging_helper = BlenderRiggingHelper()
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
            blender_rigging_helper.parent_blender_object_to_armature_with_bones_vertex_groups(
                armature_obj=blender_armature_obj,
                bones_vertex_groups=subobject.geometric_object.bone_weights,
                blender_mesh_obj=subobjects_mesh_objects[subobject.object_number]
            )
