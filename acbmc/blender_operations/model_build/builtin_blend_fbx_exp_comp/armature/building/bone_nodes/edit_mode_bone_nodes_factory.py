from typing import Tuple
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.bone_nodes_factory import BoneNodesFactory
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.blender.model.armature.edit_mode_bone_node import EditModeBoneNode


class EditModeBoneNodeDataFactory:
    @classmethod
    def get_head_and_tail_position_from(cls, transform_node: TransformNode) -> Tuple[Vector3d, Vector3d]:
        # screw the bone's orientation, who cares at the moment? :P just put something in here, we will worry later

        head_position = transform_node.position + Vector3d(x=0.1, y=0.0, z=0.0)  # type: Vector3d
        tail_position = transform_node.position + Vector3d(x=-0.1, y=0.0, z=0.0)  # type: Vector3d

        return head_position, tail_position


class EditModeBoneNodesFactory(BoneNodesFactory):
    def get_appropriate_subobject_actual_bone_node(
        self, bone_bind_pose: TransformNode, bone_name: str) -> EditModeBoneNode:
        bone_node = EditModeBoneNode()
        bone_node.bone_name = bone_name
        head_position, tail_position = EditModeBoneNodeDataFactory.get_head_and_tail_position_from(bone_bind_pose)
        bone_node.head_position = head_position
        bone_node.tail_position = tail_position
        return bone_node

    def get_appropriate_subobject_parent_bone_node(self, bone_name: str) -> EditModeBoneNode:
        bone_node = EditModeBoneNode()
        bone_node.bone_name = bone_name

        head_position, tail_position = EditModeBoneNodeDataFactory.get_head_and_tail_position_from(TransformNode())
        bone_node.head_position = head_position
        bone_node.tail_position = tail_position
        return bone_node
