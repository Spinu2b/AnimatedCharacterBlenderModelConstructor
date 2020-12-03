from typing import List
import bpy
from bpy.types import Material, MeshUVLoopLayer, Node, Object
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model.math.vector2d import Vector2d
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.subobjects.visual_data_holder import VisualDataHolder
from acbmc.model.animated_character.model.subobjects_library_desc.visual_data import VisualData


class BlenderMeshMaterialApplier:
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

        material_instance_name = UnifiedArmatureWithDeformSetsBonesNamingHelper \
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

        image_instance_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_duplicated_image_instance_name(
            subobject_number=subobject.object_number,
            material_identifier=material_identifier,
            texture_identifier=texture2d_model.texture_description_identifier,
            image_identifier=image_model.image_description_identifier
        )

        texture_image_node.image = BlenderImageHelper().get_blender_image(
            width=image_model.image_description.width,
            height=image_model.image_description.height,
            texture_image_description=image_model.image_description.pixels,
            image_name=image_instance_name
        )

        uv_loops_layer = self._apply_uv_map(
            uv_map=uv_map, mesh_blender_object=mesh_blender_object, subobject=subobject)  # type: MeshUVLoopLayer

        raise NotImplementedError
