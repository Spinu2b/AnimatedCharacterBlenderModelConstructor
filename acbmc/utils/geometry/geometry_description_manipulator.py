from typing import List

from acbmc.utils.math.vector3d import Vector3d


class GeometryDescriptionManipulator:
    @classmethod
    def scale(cls, scale_factor: float, vertices: List[Vector3d]):
        raise NotImplementedError
