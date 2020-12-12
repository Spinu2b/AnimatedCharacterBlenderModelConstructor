from typing import List
import bpy
from bpy.types import Material, MeshUVLoopLayer, Node, Object
from acbmc.util.model.blender_image_helper import BlenderImageHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .subobjects.subobjects_related_data_naming_helper import SubobjectsRelatedDataNamingHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model.math.vector2d import Vector2d
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.visual_data_holder import VisualDataHolder
from acbmc.model.animated_character.model.subobjects_library_desc.visual_data import VisualData


class BlenderMeshMaterialApplier:
    def _apply_uv_map(
        self,
        uv_map: List[Vector2d],
        uv_layer_name: str,
        mesh_blender_object: Object,
        subobject: Subobject) -> MeshUVLoopLayer:
        uv_loops_layer = mesh_blender_object.data.uv_layers.new(name=uv_layer_name)  # type: MeshUVLoopLayer

        uv_loop_index = 0
        while uv_loop_index < len(uv_map):
            first_vertex_uv = uv_map[uv_loop_index]
            second_vertex_uv = uv_map[uv_loop_index + 2]
            third_vertex_uv = uv_map[uv_loop_index + 1]

            uv_loops_layer.data[uv_loop_index].uv[0] = first_vertex_uv.x
            uv_loops_layer.data[uv_loop_index].uv[1] = first_vertex_uv.y

            uv_loops_layer.data[uv_loop_index + 1].uv[0] = second_vertex_uv.x
            uv_loops_layer.data[uv_loop_index + 1].uv[1] = second_vertex_uv.y

            uv_loops_layer.data[uv_loop_index + 2].uv[0] = third_vertex_uv.x
            uv_loops_layer.data[uv_loop_index + 2].uv[1] = third_vertex_uv.y

            uv_loop_index += 3
        
        return uv_loops_layer

    def apply(
        self,
        visual_data_holder: VisualDataHolder,
        visual_data: VisualData,
        material_identifier: str,
        uv_map: List[Vector2d],
        mesh_blender_object: Object,
        subobject: Subobject):

        # screw that, instantiate new material instance for each subobject
        # its simpler to implement and it leaves a good field for potential optimizations
        # for this control flow it is simple to refactor that later under the hood

        material_instance_name = SubobjectsRelatedDataNamingHelper \
            .get_duplicated_material_instance_name(subobject_number=subobject.object_number, material_identifier=material_identifier)

        blender_material_data_block = bpy.data.materials.new(name=material_instance_name)  # type: Material
        blender_material_data_block.use_nodes = True

        blender_material_data_block.node_tree.nodes.clear()

        # duplicate everything. We will optimize later if it will be needed
        material_output_node = blender_material_data_block \
            .node_tree.nodes.new(type="ShaderNodeOutputMaterial")  # type: Node
        material_principled_bsdf_node = blender_material_data_block \
            .node_tree.nodes.new(type="ShaderNodeBsdfPrincipled")  # type: Node
        texture_image_node = blender_material_data_block.node_tree.nodes.new(type="ShaderNodeTexImage")  # type: Node

        material_model = visual_data.materials[material_identifier]
        texture2d_model = visual_data.textures[material_model.get_one_expected_texture_identifier_or_throw_exception_in_any_other_case()]
        image_model = visual_data.images[texture2d_model.image_identifier]

        image_instance_name = SubobjectsRelatedDataNamingHelper.get_duplicated_image_instance_name(
            subobject_number=subobject.object_number,
            material_identifier=material_identifier,
            texture_identifier=texture2d_model.texture_description_identifier,
            image_identifier=image_model.image_description_identifier
        )

        texture_image_node.image = BlenderImageHelper().get_blender_image(
            width=image_model.image_description.width,
            height=image_model.image_description.height,
            texture_image_definition=image_model.image_description.pixels,
            image_name=image_instance_name
        )

        uv_layer_name = SubobjectsRelatedDataNamingHelper.get_uv_layer_name(
            subobject_number=subobject.object_number,
            material_identifier=material_identifier,
            texture_identifier=texture2d_model.texture_description_identifier,
            image_identifier=image_model.image_description_identifier
        )

        uv_loops_layer = self._apply_uv_map(
            uv_map=uv_map, uv_layer_name=uv_layer_name,
            mesh_blender_object=mesh_blender_object, subobject=subobject)  # type: MeshUVLoopLayer

        uv_map_node = blender_material_data_block.node_tree.nodes.new(type="ShaderNodeUVMap")
        uv_map_node.uv_map = uv_loops_layer.name

        blender_material_data_block.node_tree.links.new(material_output_node.inputs['Surface'], material_principled_bsdf_node.outputs['BSDF'])
        blender_material_data_block.node_tree.links.new(material_principled_bsdf_node.inputs['Base Color'], texture_image_node.outputs['Color'])
        blender_material_data_block.node_tree.links.new(texture_image_node.inputs['Vector'], uv_map_node.outputs['UV'])

        mesh_blender_object.data.materials.append(blender_material_data_block)
