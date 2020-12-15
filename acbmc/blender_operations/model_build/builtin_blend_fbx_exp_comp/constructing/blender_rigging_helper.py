from typing import Dict
from bpy.types import Object


class BlenderRiggingHelper:
    @classmethod
    def parent_blender_object_to_armature_with_bones_vertex_groups(
        cls,
        armature_obj: Object,
        blender_mesh_obj: Object,
        bones_vertex_groups: Dict[int, Dict[int, float]],
    ):
        raise NotImplementedError
