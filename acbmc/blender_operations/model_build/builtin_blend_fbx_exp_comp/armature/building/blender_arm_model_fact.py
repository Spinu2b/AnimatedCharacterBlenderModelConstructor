from typing import Dict
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.bone_nodes_factory import BoneNodesFactory
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature \
    .uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.transform_node import TransformNode


class BlenderArmatureModelFactory:
    def __init__(self, bone_nodes_factory: BoneNodesFactory):
        self.bone_nodes_factory = bone_nodes_factory

    def _complete_model_with_proper_deform_set_bones(
        self,
        subobject_number: int,
        subobject: Subobject,
        result_armature_edit_mode_model: TreeHierarchy):
        
        if subobject.contains_actual_bones():
            for bone_index, bone_bind_pose in subobject.geometric_object.bind_bone_poses.items():
                bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for(
                    bone_in_subobject_index=bone_index, subobject_number=subobject_number
                )

                bone_node = self.bone_nodes_factory.get_bone_node(bone_bind_pose, bone_name)
                #bone_node = EditModeBoneNode()
                #bone_node.bone_name = bone_name
                #head_position, tail_position = EditModeBoneNodeDataFactory.get_head_and_tail_position_from(bone_bind_pose)
                #bone_node.head_position = head_position
                #bone_node.tail_position = tail_position

                # do not parent subobjects deform set bones to one root bone yet
                result_armature_edit_mode_model.add_node(
                   parent_key=None,
                   node_key=bone_name,
                   node=bone_node
                )
        else:
            bone_name = \
                UnifiedArmatureWithDeformSetsBonesNamingHelper.get_mock_bone_name_for_object_parenting(
                    subobject_number=subobject_number
                )

            bone_node = self.bone_nodes_factory.get_home_transformed_bone_node(bone_name)
            # bone_node = EditModeBoneNode()
            # bone_node.bone_name = bone_name


            # do not parent subobjects deform set bones to one root bone yet
            result_armature_edit_mode_model.add_node(
               parent_key=None,
               node_key=bone_name,
               node=bone_node
            )
    
    def get_blender_armature_model(self, data: any) -> TreeHierarchy:
        result = TreeHierarchy()

        subobjects = data  # type: Dict[int, Subobject]

        # root_bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_root_channel()

        # root_bone_node = self.bone_nodes_factory.get_home_transformed_bone_node(root_bone_name)
        # root_bone_node = EditModeBoneNode()
        # root_bone_node.bone_name = root_bone_name

        # result.add_node(
        #    parent_key=None,
        #    node_key=root_bone_name,
        #    node=root_bone_node)

        for subobject_number in subobjects:
            subobj = subobjects[subobject_number]  # type: Subobject
            self._complete_model_with_proper_deform_set_bones(subobject_number, subobj, result)

        return result
