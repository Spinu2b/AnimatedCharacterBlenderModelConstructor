

class UnifiedArmatureWithDeformSetsBonesNamingHelper:
    @staticmethod
    def get_bone_name_for(
        bone_in_subobject_index: int, channel_id: int, subobject_number: int) -> str:
        return "BONE_Subobject_{}_Bone_{}".format(subobject_number, bone_in_subobject_index)

    @staticmethod
    def get_mock_bone_name_for_object_parenting(channel_id: int, subobject_number: int) -> str:
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
    def is_deform_set_bone(bone_name: str) -> bool:
        return bone_name.startswith('BONE_Subobject_')

    @staticmethod
    def get_subobject_name(subobject_number: int) -> str:
        return "SUBOBJECT_{}".format(subobject_number)

    @staticmethod
    def get_duplicated_material_instance_name(subobject_number: int, material_identifier: str) -> str:
        raise NotImplementedError

    @staticmethod
    def get_duplicated_image_instance_name(
        subobject_number: int,
        material_identifier: str,
        texture_identifier: str,
        image_identifier: str) -> str:
        raise NotImplementedError
