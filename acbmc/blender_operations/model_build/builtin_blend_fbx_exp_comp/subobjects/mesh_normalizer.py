import bpy
from bpy.types import Object
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator


class MeshNormalizer:
    @classmethod
    def normalize_mesh(cls, blender_mesh_object: Object):
        blender_editor_manipulator = BlenderEditorManipulator()
        blender_editor_manipulator.enter_edit_mode_for_object_as_active_from_object_mode(blender_mesh_object)

        cls._merge_duplicated_vertices_by_distance()
        blender_editor_manipulator.enter_object_mode()
        cls._shade_smooth()

    @classmethod
    def _merge_duplicated_vertices_by_distance(cls):
        bpy.ops.mesh.remove_doubles()

    @classmethod
    def _shade_smooth(cls):
        bpy.context.object.data.polygons.foreach_set('use_smooth',  [True] * len(bpy.context.object.data.polygons))
