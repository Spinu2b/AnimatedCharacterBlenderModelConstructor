from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.constructing.math.quaternion_factory import QuaternionFactory
from acbmc.model.animated_character.constructing.math.vector3d_factory import Vector3dFactory


class BoneBindPoseFactory:
    def construct_from_json_dict(self, bone_bind_pose_json_dict) -> TransformNode:
        vector3d_factory = Vector3dFactory()
        quaternion_factory = QuaternionFactory()

        result = TransformNode()
        result.position = vector3d_factory.construct_from_json_dict(bone_bind_pose_json_dict["position"])
        result.rotation = quaternion_factory.construct_from_json_dict(bone_bind_pose_json_dict["rotation"])
        result.scale = vector3d_factory.construct_from_json_dict(bone_bind_pose_json_dict["scale"])
        return result
