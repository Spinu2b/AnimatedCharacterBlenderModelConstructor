from acbmc.model.constructing.math.quaternion_factory import QuaternionFactory
from acbmc.model.constructing.math.vector3d_factory import Vector3dFactory
from acbmc.model.model.subobjects_library_desc.subobject_desc.geo_obj_desc.bone_bind_pose import BoneBindPose


class BoneBindPoseFactory:
    def construct_from_json_dict(self, bone_bind_pose_json_dict) -> BoneBindPose:
        vector3d_factory = Vector3dFactory()
        quaternion_factory = QuaternionFactory()

        result = BoneBindPose()
        result.position = vector3d_factory.construct_from_json_dict(bone_bind_pose_json_dict["position"])
        result.rotation = quaternion_factory.construct_from_json_dict(bone_bind_pose_json_dict["rotation"])
        result.scale = vector3d_factory.construct_from_json_dict(bone_bind_pose_json_dict["scale"])
        return result
