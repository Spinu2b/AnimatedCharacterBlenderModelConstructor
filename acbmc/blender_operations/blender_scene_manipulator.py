import bpy

class BlenderSceneManipulator:
    def clear_scene(self):
        bpy.ops.wm.read_homefile(use_empty=True)
