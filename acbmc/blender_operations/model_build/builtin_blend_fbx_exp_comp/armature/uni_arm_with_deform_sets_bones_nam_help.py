

class UnifiedArmatureWithDeformSetsBonesNamingHelper:
    @staticmethod
    def get_bone_name_for(
        bone_in_subobject_index: int, channel_id: int, subobject_number: int) -> str:
        return "BONE_Subobject_{}_Bone_{}".format(subobject_number, bone_in_subobject_index)

    @staticmethod
    def get_mock_bone_name_for_object_parenting(channel_id: int, subobject_number: int) -> str:
        return "BONE_Subobject_{}".format(subobject_number)
