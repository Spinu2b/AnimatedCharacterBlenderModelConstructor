

class UnifiedArmatureWithDeformSetsBonesNamingHelper:
    @staticmethod
    def get_bone_name_for(
        bone_in_subobject_index: int, subobject_number: int) -> str:
        return "BONE_Subobject_{}_Bone_{}".format(subobject_number, bone_in_subobject_index)

    @staticmethod
    def get_mock_bone_name_for_object_parenting(subobject_number: int) -> str:
        return "BONE_Subobject_{}".format(subobject_number)

    @staticmethod
    def get_bone_name_for_channel_id(channel_id: int) -> str:
        return "BONE_Channel_{}".format(channel_id)

    @staticmethod
    def get_bone_name_for_root_channel() -> str:
        return "BONE_Channel_ROOT"

    @staticmethod
    def is_channel_bone_name(bone_name: str) -> bool:
        return bone_name.startswith('BONE_Channel_')

    @staticmethod
    def get_channel_id_from_channel_bone_name(bone_name: str) -> int:
        raise NotImplementedError

    @staticmethod
    def is_deform_set_bone(bone_name: str) -> bool:
        return bone_name.startswith('BONE_Subobject_')

    @staticmethod
    def get_animation_clip_name_for(animation_clip_id: int) -> str:
        return "ANIMATION_CLIP_{}".format(animation_clip_id)
