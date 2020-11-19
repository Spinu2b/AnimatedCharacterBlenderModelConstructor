from acbmc.util.model.transform_node import TransformNode
from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode


class BoneAbsoluteTransformNodeFactory:
    @staticmethod
    def get_from_bind_bone_pose(bone_name: str, bind_bone_pose: TransformNode) -> BoneAbsoluteTransformNode:
        result = BoneAbsoluteTransformNode()
        result.bone_name = bone_name
        result.bone_transform = bind_bone_pose.copy()
        return result
