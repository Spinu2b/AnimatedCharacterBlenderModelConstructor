import bpy
from bpy.types import Object
from acbmc.blender_operations.blender_objects_manipulator import BlenderObjectsManipulator

class BlenderEditorManipulator:
    def enter_edit_mode_for_object_as_active_from_object_mode(self, object: Object):
        blender_objects_manipulator = BlenderObjectsManipulator()
        # blender_objects_manipulator.deselect_all_objects()
        blender_objects_manipulator.set_active_object_to(object)
        blender_objects_manipulator.select_active_object(object)
        self.enter_edit_mode()

    def enter_edit_mode(self):
        bpy.ops.object.mode_set(mode='EDIT')

    def enter_object_mode(self):
        bpy.ops.object.mode_set(mode='OBJECT')
