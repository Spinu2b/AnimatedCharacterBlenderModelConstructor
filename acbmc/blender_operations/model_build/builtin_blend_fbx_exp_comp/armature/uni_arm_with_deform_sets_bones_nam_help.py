import re
from typing import Tuple
from acbmc.util.regex_patterns import NUMBER_PATTERN

class UnifiedArmatureWithDeformSetsBonesNamingHelper:
    DEFORM_SET_ACTUAL_BONE_PATTERN = "^BONE_Subobject_{}_Bone_{}$".format(NUMBER_PATTERN, NUMBER_PATTERN)
    SUBOBJECT_GOVERNING_BONE_PATTERN = "^BONE_Subobject_{}$".format(NUMBER_PATTERN)

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
        return int(re.findall(NUMBER_PATTERN, bone_name)[0])

    @staticmethod
    def is_deform_set_bone(bone_name: str) -> bool:
        return bone_name.startswith('BONE_Subobject_')

    @classmethod
    def is_deform_set_subobject_governing_bone(cls, bone_name: str) -> bool:
        return bool(re.match(cls.SUBOBJECT_GOVERNING_BONE_PATTERN, bone_name))

    @classmethod
    def is_deform_set_actual_bone(cls, bone_name: str) -> bool:
        return bool(re.match(cls.DEFORM_SET_ACTUAL_BONE_PATTERN, bone_name))

    @staticmethod
    def get_subobject_index_and_bone_index_for_subobject_deform_set_bone(bone_name: str) -> Tuple[int, int]:
        found_numbers = [int(x) for x in re.findall(NUMBER_PATTERN, bone_name)]
        return found_numbers[0], found_numbers[1]

    @staticmethod
    def get_subobject_index_for_subobject_governing_bone(bone_name: str) -> int:
        return int(re.findall(NUMBER_PATTERN, bone_name)[0])

    @staticmethod
    def get_animation_clip_name_for(animation_clip_id: int) -> str:
        return "ANIMATION_CLIP_{}".format(animation_clip_id)
