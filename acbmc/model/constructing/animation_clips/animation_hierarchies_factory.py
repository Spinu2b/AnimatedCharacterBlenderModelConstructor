from acbmc.model.constructing.animation_clips.animation_frames_period_info_factory import AnimationFramesPeriodInfoFactory
from typing import Dict, List
from acbmc.model.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo


class AnimationHierarchiesFactory:
    def construct_from_json_dict(self, animation_hierarchies_json_dict) -> Dict[str, List[AnimationFramesPeriodInfo]]:
        result = dict()  # type: Dict[str, List[AnimationFramesPeriodInfo]]
        animation_frames_period_info_factory = AnimationFramesPeriodInfoFactory()
        for animation_hierarchy_identifier in animation_hierarchies_json_dict:
            result[animation_hierarchy_identifier] = []
            for animation_frames_period_info_json_dict in animation_hierarchies_json_dict[animation_hierarchy_identifier]:
                result[animation_hierarchy_identifier].append(
                    animation_frames_period_info_factory.construct_from_json_dict(
                        animation_frames_period_info_json_dict))
        return result
