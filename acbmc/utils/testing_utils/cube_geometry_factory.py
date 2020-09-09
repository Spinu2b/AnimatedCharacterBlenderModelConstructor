from typing import List

from acbmc.utils.math.vector3d import Vector3d


class CubeGeometryFactory:
    def get_cube_default_vertices(self) -> List[Vector3d]:
        raise NotImplementedError
