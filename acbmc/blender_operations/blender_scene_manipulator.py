import bpy

class BlenderSceneManipulator:
    def clear_scene(self):
        # bpy.ops.wm.read_homefile(use_empty=True)

        # lets go dirty here and just assume we have default Blender scene
        # lets remove default cube, camera and light to have basically the clear scene and proper context to work with

        objs = [bpy.context.scene.objects['Camera'], bpy.context.scene.objects['Cube'], bpy.context.scene.objects['Light']]
        bpy.ops.object.delete({"selected_objects": objs})
