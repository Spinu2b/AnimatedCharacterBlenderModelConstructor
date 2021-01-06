from typing import Callable, Dict, List
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.model.math.vector2d import Vector2d
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class GeometricObject:
    def __init__(self):
        self.vertices = []  # type: List[Vector3d]
        self.normals = []  # type: List[Vector3d]
        self.triangles = []  # type: List[int]
        self.uv_maps = []  # type: List[List[Vector2d]]
        self.material = None  # type: str

        self.bind_bone_poses = dict()  # type: Dict[int, TransformNode]
        self.bone_weights = dict()  # Dict[int, Dict[int, float]]

    def contains_actual_bones(self) -> bool:
        return len(self.bind_bone_poses) != 0

    def reform_space_model(
        self,
        position3d_transformation: Callable[[Vector3d], None],
        rotation_transformation: Callable[[Quaternion], None]):

        for vertex in self.vertices:
            position3d_transformation(vertex)

        for normal in self.normals:
            position3d_transformation(normal)

        for bind_pose in self.bind_bone_poses.values():
            bind_pose.reform_space_model(
                position3d_transformation=position3d_transformation,
                rotation_transformation=rotation_transformation
            )
