from acbmc.util.model.matrix4x4 import Matrix4x4
from acbmc.util.model.transform_node import TransformNode


class BoneTransformNode:
    def __init__(self):
        self.bone_name = None  # type: str
        self.bone_transform = TransformNode()
        self.is_keyframe = False

    def copy(self) -> 'BoneTransformNode':
        result = BoneTransformNode()
        result.bone_name = self.bone_name
        result.bone_transform = self.bone_transform.copy()
        return result

    @staticmethod
    def from_transform_node(bone_name: str, transform_node: TransformNode, is_keyframe: bool=False) -> 'BoneTransformNode':
        result = BoneTransformNode()
        result.bone_name = bone_name
        result.bone_transform = transform_node.copy()
        result.is_keyframe = is_keyframe
        return result

    @staticmethod
    def from_matrix4x4(bone_name: str, matrix: Matrix4x4, is_keyframe: bool=False) -> 'BoneTransformNode':
        result = BoneTransformNode()
        result.bone_name = bone_name
        result.bone_transform = TransformNode.from_matrix4x4(matrix)
        result.is_keyframe = is_keyframe
        return result

    @classmethod
    def get_zero_transform_with_bone_name(cls, bone_name: str) -> 'BoneTransformNode':
        return cls.from_transform_node(bone_name=bone_name, transform_node=TransformNode())
