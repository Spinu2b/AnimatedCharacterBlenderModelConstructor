from typing import Tuple
from bpy.types import Armature, Object
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.armature.blender_arm_bone_creat_manip import BlenderArmatureBoneCreationManipulator
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.armature.blender_armature_manipulator import BlenderArmatureManipulator
from acbmc.model.blender.model.armature.edit_mode_bone_node import EditModeBoneNode


class BlenderArmatureGenerator:
    def create_armature(self, name: str) -> Tuple[Armature, Object]:
        blender_armature_manipulator = BlenderArmatureManipulator()
        return blender_armature_manipulator.create_armature(name=name)

    def place_bone(
        self,
        armature_obj: Object,
        armature: Armature,
        edit_mode_bone_node: EditModeBoneNode):
        blender_armature_bone_creation_manipulator = BlenderArmatureBoneCreationManipulator()
        blender_editor_manipulator = BlenderEditorManipulator()
        # blender_editor_manipulator.enter_edit_mode()
        blender_armature_bone_creation_manipulator.add_bone(
            head_position=edit_mode_bone_node.head_position,
            tail_position=edit_mode_bone_node.tail_position,
            name=edit_mode_bone_node.bone_name,
            armature=armature,
            armature_obj=armature_obj
        )

    def parent_bone_to(
        self,
        child: str,
        parent: str,
        armature: Armature
    ):
        blender_armature_bone_creation_manipulator = BlenderArmatureBoneCreationManipulator()
        #if parent is not None:
        blender_armature_bone_creation_manipulator.parent_bone_to(
            child_bone_name=child,
            parent_bone_name=parent,
            armature=armature
        )
