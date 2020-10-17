from typing import Dict, List
from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geo_obj_desc.bone_bind_pose import BoneBindPose
from acbmc.model.animated_character.model.math.vector2d import Vector2d
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class GeometricObject:
    def __init__(self):
        self.vertices = []  # type: List[Vector3d]
        self.normals = []  # type: List[Vector3d]
        self.triangles = []  # type: List[int]
        self.uv_maps = []  # type: List[List[Vector2d]]
        self.material = None  # type: str

        self.bind_bone_poses = dict()  # type: Dict[int, BoneBindPose]
        self.bone_weights = dict()  # Dict[int, Dict[int, float]]
