from typing import Iterable, List, Tuple
from acbmc.model.animated_character.model \
    .subobjects_library_desc.subobject_desc.geometric_object import GeometricObject


class BlenderMeshGeometryFactory:
    @classmethod
    def _get_blender_edges_list(cls, triangles: List[int]) -> List[Tuple[int, int]]:
        result = []  # type: List[Tuple[int, int]]
        triangles_list_elem_index = 0
        while triangles_list_elem_index < len(triangles) - 2:
            # Here might be the bug, check if you actually have legitimately valid edges indices pairs, if they do not repeat
            # regardless of order etc. Blender actually has assertion enabled in mesh validation in debug variant

            # _BLI_assert_print_backtrace D:\BlenderProject\blender_newest\blender\source\blender\blenlib\intern\BLI_assert.c:39
            # blender::Map<blender::bke::calc_edges::OrderedEdge,blender::bke::calc_edges::OrigEdgeOrIndex,4,blen D:\BlenderProject\blender_newest\blender\source\blender\blenlib\BLI_map.hh:964
            # blender::Map<blender::bke::calc_edges::OrderedEdge,blender::bke::calc_edges::OrigEdgeOrIndex,4,blen D:\BlenderProject\blender_newest\blender\source\blender\blenlib\BLI_map.hh:252
            # blender::Map<blender::bke::calc_edges::OrderedEdge,blender::bke::calc_edges::OrigEdgeOrIndex,4,blen D:\BlenderProject\blender_newest\blender\source\blender\blenlib\BLI_map.hh:238
            # <lambda_0f72d67394915732a5b660516877bfdb>::operator() D:\BlenderProject\blender_newest\blender\source\blender\blenkernel\intern\mesh_validate.cc:107

            # the error is thrown at the moment when trying to add same element again, in this case the OrderedEdge (with int v_low, v_high)
            # hint -> write validation for your pairs lists if they do not contain duplicated elements to check where you did logical error
            # or check at all if you have pairs with same indices, regardless of order
            
            result.append((triangles[triangles_list_elem_index], triangles[triangles_list_elem_index + 1]))
            result.append((triangles[triangles_list_elem_index + 1], triangles[triangles_list_elem_index + 2]))
            result.append((triangles[triangles_list_elem_index + 2], triangles[triangles_list_elem_index]))
            triangles_list_elem_index += 3
        
        return result

    @classmethod
    def _get_blender_triangles_list(cls, triangles: List[int]) -> List[Tuple[int, int, int]]:
        result = []  # type: List[Tuple[int, int, int]]
        triangles_list_elem_index = 0
        while triangles_list_elem_index < len(triangles):
            if triangles_list_elem_index < len(triangles) - 2:
                result.append(
                    (triangles[triangles_list_elem_index],
                     triangles[triangles_list_elem_index + 1],
                     triangles[triangles_list_elem_index + 2]))
            triangles_list_elem_index += 3

        return result

    @classmethod
    def get_from_geometric_object(cls, geometric_object: GeometricObject) \
         -> Tuple[Iterable[Tuple[float, float, float]], Iterable[Tuple[int, int]], Iterable[Tuple[int, int, int]]]:
        vertices_list = [(v.x, v.y, v.z) for v in geometric_object.vertices]  # type: List[Tuple[float, float, float]]
        edges_list = cls._get_blender_edges_list(geometric_object.triangles)
        triangles_list = cls._get_blender_triangles_list(geometric_object.triangles)
        return vertices_list, edges_list, triangles_list
