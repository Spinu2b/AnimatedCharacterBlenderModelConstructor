import bpy
from bpy.types import Action, Object
from acbmc.blender_operations.blender_objects_manipulator import BlenderObjectsManipulator

class BlenderEditorManipulator:
    def enter_edit_mode_for_object_as_active_from_object_mode(self, object: Object):
        blender_objects_manipulator = BlenderObjectsManipulator()
        # blender_objects_manipulator.deselect_all_objects()
        blender_objects_manipulator.set_active_object_to(object)
        blender_objects_manipulator.select_active_object(object)
        self.enter_edit_mode()

    def enter_pose_mode_for_object_as_active_from_object_mode(self, object: Object):
        blender_objects_manipulator = BlenderObjectsManipulator()
        # blender_objects_manipulator.deselect_all_objects()
        blender_objects_manipulator.set_active_object_to(object)
        blender_objects_manipulator.select_active_object(object)
        self.enter_pose_mode()

    def enter_edit_mode(self):
        bpy.ops.object.mode_set(mode='EDIT')

    def enter_object_mode(self):
        bpy.ops.object.mode_set(mode='OBJECT')

    def enter_pose_mode(self):
        bpy.ops.object.mode_set(mode="POSE")

    def set_context_area_ui_type_to_dopesheet(self):
        bpy.context.area.ui_type = 'DOPESHEET'

    def set_context_space_data_ui_mode_to_action(self):
        bpy.context.space_data.ui_mode = 'ACTION'

    def enter_animation_clip(self, name: str) -> Action:
        action = bpy.data.actions.new(name=name)  # type: Action
        action.use_fake_user = True
        return action

    def set_armature_active_action(self, armature_obj: Object, action: Action):
        bpy.context.space_data.action = action

    def enter_frame_number(self, frame_number: int):
        bpy.context.scene.frame_current = frame_number
