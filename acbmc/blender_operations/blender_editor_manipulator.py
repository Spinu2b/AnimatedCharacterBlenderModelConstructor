import bpy

class BlenderEditorManipulator:
    def enter_edit_mode(self):
        bpy.ops.object.mode_set(mode='EDIT')
