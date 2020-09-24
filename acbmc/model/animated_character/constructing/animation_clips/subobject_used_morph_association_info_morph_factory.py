from typing import Dict, List
from acbmc.model.animated_character.model.animation_clips_desc.subobject_used_morph_association_info import SubobjectUsedMorphAssociationInfo


class SubobjectUsedMorphAssociationInfoFactory:
    def _get_morph_progress_keyframes(morph_progress_keyframes_json_dict) -> Dict[int, float]:
        raise NotImplementedError

    def construct_from_json_dict(self, subobject_used_morph_association_info_json_dict) -> SubobjectUsedMorphAssociationInfo:
        result = SubobjectUsedMorphAssociationInfo()
        result.morph_subobject_start = subobject_used_morph_association_info_json_dict["morphSubobjectStart"]
        result.morph_subobject_end = subobject_used_morph_association_info_json_dict["morphSubobjectEnd"]
        result.morph_progress_keyframes = self._get_morph_progress_keyframes(subobject_used_morph_association_info_json_dict["morphProgressKeyframes"])
        return result


class SubobjectUsedMorphAssociationInfoMorphFactory:
    def construct_from_json_dict(self, subobject_used_morph_association_info_morph_json_dict) -> List[SubobjectUsedMorphAssociationInfo]:
        result = []  # type: List[SubobjectUsedMorphAssociationInfo]
        subobject_used_morph_association_info_factory = SubobjectUsedMorphAssociationInfoFactory()
        for subobject_used_morph_association_info_json_dict in subobject_used_morph_association_info_morph_json_dict:
            result.append(subobject_used_morph_association_info_factory.construct_from_json_dict(subobject_used_morph_association_info_json_dict))
        return result
