from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode
from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geo_obj_desc.bone_bind_pose import BoneBindPose


class BoneAbsoluteTransformNodeFactory:
    @staticmethod
    def get_from_bind_bone_pose(bone_name: str, bind_bone_pose: BoneBindPose) -> BoneAbsoluteTransformNode:
        raise NotImplementedError
