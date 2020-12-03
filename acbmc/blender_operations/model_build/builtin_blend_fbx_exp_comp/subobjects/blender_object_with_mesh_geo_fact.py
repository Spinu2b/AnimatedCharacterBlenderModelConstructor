from typing import List
import bpy
from bpy.types import Mesh, Object
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.visual_data_holder import VisualDataHolder
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.blender_mesh_material_applier import BlenderMeshMaterialApplier
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .subobjects.blender_mesh_geometry_fact import BlenderMeshGeometryFactory
from acbmc.blender_operations.blender_objects_manipulator import BlenderObjectsManipulator
from acbmc.model.animated_character.model.subobjects_library_desc \
    .subobject_desc.geometric_object import GeometricObject
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.subobjects_library_desc.visual_data import VisualData


class BlenderObjectWithMeshGeometryFactory:
    @classmethod
    def _apply_normals(cls, subobject: Subobject, mesh_object: Object):
        normals_definitions = subobject.geometric_object.normals  # type: List[Vector3d]
        for mesh_vertex_index, mesh_vertex in enumerate(mesh_object.data.vertices):
            mesh_vertex.normal[0] = normals_definitions[mesh_vertex_index].x
            mesh_vertex.normal[1] = normals_definitions[mesh_vertex_index].y
            mesh_vertex.normal[2] = normals_definitions[mesh_vertex_index].z

    @classmethod
    def _apply_mesh_materials(
        cls,
        visual_data: VisualData,
        visual_data_holder: VisualDataHolder,
        subobject: Subobject,
        mesh_object: Object):
        blender_mesh_material_applier = BlenderMeshMaterialApplier()
        blender_mesh_material_applier.apply(
            visual_data=visual_data,
            visual_data_holder=visual_data_holder,
            material_identifier=subobject.geometric_object.material,
            uv_map=subobject.geometric_object.uv_maps[0],
            mesh_blender_object=mesh_object,
            subobject=subobject
        )

    @classmethod
    def create_from_subobject_desc(
        cls,
        visual_data: VisualData,
        visual_data_holder: VisualDataHolder,
        subobject_number: int,
        subobject: Subobject) -> Object:
        blender_objects_manipulator = BlenderObjectsManipulator()

        subobject_core_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_subobject_name(subobject_number)  # type: str

        mesh_data_block = bpy.data.meshes.new(name=subobject_core_name)  # type: Mesh
        mesh_object = blender_objects_manipulator.create_new_object_with_linked_datablock(
            object_name="OBJECT_" + subobject_core_name, data_block=mesh_data_block
        )  # type: Object
        blender_objects_manipulator.link_object_to_the_scene(mesh_object)

        blender_objects_manipulator.deselect_all_objects()
        blender_objects_manipulator.set_active_object_to(mesh_object)
        blender_objects_manipulator.select_active_object()

        mesh_geometry = subobject.geometric_object  # type: GeometricObject
        vertices, edges, faces = BlenderMeshGeometryFactory.get_from_geometric_object(mesh_geometry)

        mesh_object.data.from_pydata(vertices, edges, faces)
        cls._apply_normals(subobject, mesh_object)
        cls._apply_mesh_materials(
            visual_data=visual_data,
            visual_data_holder=visual_data_holder,
            subobject=subobject,
            mesh_object=mesh_object)
        return mesh_object
