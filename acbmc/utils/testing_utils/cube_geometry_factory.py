from typing import List, Generator

from acbmc.utils.math.vector3d import Vector3d


class CubeGeometryVerticesFactory:
    @classmethod
    def iterate_default_cube_vertices(cls) -> Generator[Vector3d]:
        for x in [-1, 1]:
            for y in [-1, 1]:
                for z in [-1, 1]:
                    yield Vector3d(x, y, z)


class CubeGeometryFactory:
    def get_cube_default_vertices(self) -> List[Vector3d]:
        return [vertex for vertex in CubeGeometryVerticesFactory.iterate_default_cube_vertices()]
