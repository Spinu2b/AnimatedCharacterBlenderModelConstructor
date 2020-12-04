from typing import Dict
from acbmc.model.animated_character.model.animation_clips import AnimationClips
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject


class SubobjectsMorphUsageHelper:
    @classmethod
    def get_core_actual_subobjects_considering_morph_data(
        cls,
        animation_clips: AnimationClips,
        subobjects: Dict[int, Subobject]) -> Dict[int, Subobject]:
        raise NotImplementedError
