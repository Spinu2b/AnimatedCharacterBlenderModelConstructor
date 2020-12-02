from typing import Iterable, List, Tuple
from acbmc.model.animated_character.model \
    .subobjects_library_desc.subobject_desc.geometric_object import GeometricObject


class BlenderMeshGeometryFactory:
    @classmethod
    def get_from_geometric_object(cls, geometric_object: GeometricObject) \
         -> Tuple[Iterable[Tuple[float, float, float]], Iterable[Tuple[int, int]], Iterable[Tuple[int, int, int]]]:
        def flatten(object):
            for item in object:
                if isinstance(item, (list)):
                    yield from flatten(item)
                else:
                    yield item

        vertices_list = [(v.x, v.y, v.z) for v in geometric_object.vertices]  # type: List[Tuple[float, float, float]]
        edges_list = [list(x) for x in list(set(flatten([[frozenset([f[0], f[1]]), frozenset([f[1], f[2]]),
                                                          frozenset([f[2], f[0]])] for f in
                                                         geometric_object.triangles])))]  # type: List[Tuple[int, int]]
        triangles_list = [(f[0], f[1], f[2]) for f in geometric_object.triangles]  # type: List[Tuple[int, int, int]]
        return vertices_list, edges_list, triangles_list
