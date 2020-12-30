from typing import Tuple
import bpy
from bpy.types import Armature, Object
from acbmc.blender_operations.blender_objects_manipulator import BlenderObjectsManipulator


class BlenderArmatureManipulator:
    def create_armature(self, name: str) -> Tuple[Armature, Object]:
        blender_objects_manipulator = BlenderObjectsManipulator()
        armature = bpy.data.armatures.new(name=name)
        armature_obj = blender_objects_manipulator.create_new_object_with_linked_datablock(
            object_name=name + "_OBJECT", data_block=armature
        )
        blender_objects_manipulator.link_object_to_the_scene(armature_obj)
        blender_objects_manipulator.deselect_all_objects()
        blender_objects_manipulator.set_active_object_to(armature_obj)
        blender_objects_manipulator.select_active_object(armature_obj)
        return armature, armature_obj
