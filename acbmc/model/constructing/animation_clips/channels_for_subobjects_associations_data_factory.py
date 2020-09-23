from typing import Dict, List
from acbmc.model.constructing.animation_clips.animation_frames_period_info_factory import AnimationFramesPeriodInfoFactory
from acbmc.model.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo


class ChannelsForSubobjectsAssociationsDataFactory:
    def construct_from_json_dict(self, 
        channels_for_subobjects_associations_data_json_dict) -> Dict[str, List[AnimationFramesPeriodInfo]]:
        result = dict()  # type: Dict[str, List[AnimationFramesPeriodInfo]]
        animation_frames_period_info_factory = AnimationFramesPeriodInfoFactory()
        for channels_subobjects_association_identifier in channels_for_subobjects_associations_data_json_dict:
            result[channels_subobjects_association_identifier] = []
            for animation_frames_period_info_json_dict in \
                channels_for_subobjects_associations_data_json_dict[channels_subobjects_association_identifier]:
                result[channels_subobjects_association_identifier].append(
                    animation_frames_period_info_factory.construct_from_json_dict(animation_frames_period_info_json_dict))
        return result

