from typing import Dict, List
from acbmc.model.animated_character.model.animation_clips_desc \
    .subobject_used_morph_association_info import SubobjectUsedMorphAssociationInfo
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip
from acbmc.model.animated_character.model.animation_clips import AnimationClips
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject


class MorphDataHelper:
    @classmethod
    def get_starting_morph_target_subobjects_numbers_list(animation_clips: Dict[int, AnimationClip]) -> List[int]:
        morph_data_list_of_lists = [anim_clip.morphs for anim_clip in animation_clips.values()]  # List[List[SubobjectUsedMorphAssociationInfo]]
        morph_data_flattened_list = [morph for morph_data in 
            morph_data_list_of_lists for morph in morph_data]  # type: List[SubobjectUsedMorphAssociationInfo]
        
        return [morph.morph_subobject_start for morph in morph_data_flattened_list]


class SubobjectsMorphUsageHelper:
    @classmethod
    def _has_any_actual_morph_data_at_all(cls, animation_clips: Dict[int, AnimationClip]) -> bool:
        return any(len(anim_clip.morphs) != 0 for anim_clip in animation_clips.values())

    @classmethod
    def _get_subobjects_that_are_typed_as_starting_morph_subobject_target(
        cls, subobjects: Dict[int, Subobject], animation_clips: Dict[int, AnimationClip]) -> Dict[int, Subobject]:
        starting_morph_subobjects_numbers_list = MorphDataHelper.get_starting_morph_target_subobjects_numbers_list(animation_clips)
        return {subobj.object_number: subobj for subobj 
            in subobjects.values() if subobj.object_number in starting_morph_subobjects_numbers_list}

    @classmethod
    def get_core_actual_subobjects_considering_morph_data(
        cls,
        animation_clips: AnimationClips,
        subobjects: Dict[int, Subobject]) -> Dict[int, Subobject]:
        
        animation_clips_dict = animation_clips.animation_clips  # type: Dict[int, AnimationClip]

        result = None  # type: Dict[int, Subobject]
        if not cls._has_any_actual_morph_data_at_all(animation_clips_dict):
            result = subobjects
        else:
            result = cls._get_subobjects_that_are_typed_as_starting_morph_subobject_target(subobjects, animation_clips_dict)

        return result
