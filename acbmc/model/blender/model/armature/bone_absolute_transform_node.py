from acbmc.util.model.transform_node import TransformNode


class BoneAbsoluteTransformNode:
    def __init__(self):
        self.bone_name = None  # type: str
        self.bone_transform = TransformNode()

    def copy(self) -> 'BoneAbsoluteTransformNode':
        result = BoneAbsoluteTransformNode()
        result.bone_name = self.bone_name
        result.bone_transform = self.bone_transform.copy()
        return result

    @staticmethod
    def from_transform_node(bone_name: str, transform_node: TransformNode) -> 'BoneAbsoluteTransformNode':
        result = BoneAbsoluteTransformNode()
        result.bone_name = bone_name
        result.bone_transform = transform_node.copy()
        return result

    @classmethod
    def get_zero_transform_with_bone_name(cls, bone_name: str) -> 'BoneAbsoluteTransformNode':
        return cls.from_transform_node(bone_name=bone_name, transform_node=TransformNode())
