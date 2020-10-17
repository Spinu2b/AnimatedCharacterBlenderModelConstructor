from typing import Any, Callable, Dict, List, Set
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChannelTransformHelper:
    @staticmethod
    def interpolate_linear_for_frame(frame_number: int, channel_timeline_keyframes: Dict[int, ChannelTransform]) -> ChannelTransform:
        raise NotImplementedError


class AnimationFramesPeriodedAnimClipDataHelper:
    def find_matching_store_data(
        frame_number: int,  
        animation_clip_frames_periods_data: Dict[str, List[AnimationFramesPeriodInfo]],
        string_identifiable_data_store: Dict[str, Any],
        match_return_lambda: Callable[[Any], Any],
        not_found_error_lambda: Callable[[],]) -> Any:
        for data_store_part_identifier, animation_frames_period_infos_list in animation_clip_frames_periods_data.items():
            if any(x.contains_frame_number(frame_number) for x in animation_frames_period_infos_list):
                return match_return_lambda(string_identifiable_data_store[data_store_part_identifier])
        raise not_found_error_lambda()        
    

class AnimationClipModelPartsFetchingHelper:
    @staticmethod
    def get_channels_set_for_frame(
        frame_number: int,
        animation_hierarchies: Dict[str, List[AnimationFramesPeriodInfo]],
        channel_hierarchies: Dict[str, ChannelHierarchy]) -> Set[int]:

        return AnimationFramesPeriodedAnimClipDataHelper.find_matching_store_data(
            frame_number=frame_number,
            animation_clip_frames_periods_data=animation_hierarchies,
            string_identifiable_data_store=channel_hierarchies,
            match_return_lambda=lambda x: x.channel_hierarchy.channels,
            not_found_error_lambda=lambda: ValueError(
                "Did not find any matching animation hierarchy that would fit for that frame number! {}".format(frame_number))
        )

    @staticmethod
    def get_channel_transforms_for_frame(
        frame_number: int,
        channel_keyframes: Dict[int, Dict[int, ChannelTransform]]) -> Dict[int, ChannelTransform]:
        
        result = dict()  # type: Dict[int, ChannelTransform]
        for channel_identifier in channel_keyframes:
            result[channel_identifier] = \
                ChannelTransformHelper.interpolate_linear_for_frame(
                    frame_number=frame_number,
                    channel_timeline_keyframes=channel_keyframes[channel_identifier]
                )
        return result    

    @staticmethod    
    def get_channels_for_subobjects_association_for_frame(
        frame_number: int,
        channels_for_subobjects_associations_data: Dict[str, List[AnimationFramesPeriodInfo]],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation]) -> SubobjectsChannelsAssociation:

        return AnimationFramesPeriodedAnimClipDataHelper.find_matching_store_data(
            frame_number=frame_number,
            animation_clip_frames_periods_data=channels_for_subobjects_associations_data,
            string_identifiable_data_store=subobjects_channels_associations,
            match_return_lambda=lambda x: x,
            not_found_error_lambda=lambda: ValueError(
                "Did not find any matching subobjects channels association that would fit for that frame number! {}".format(frame_number))
        )

    @staticmethod    
    def get_channel_hierarchy_for_frame(
        frame_number: int,
        animation_hierarchies: Dict[str, List[AnimationFramesPeriodInfo]],
        channel_hierarchies: Dict[str, ChannelHierarchy]) -> ChannelHierarchy:

        return AnimationFramesPeriodedAnimClipDataHelper.find_matching_store_data(
            frame_number=frame_number,
            animation_clip_frames_periods_data=animation_hierarchies,
            string_identifiable_data_store=channel_hierarchies,
            match_return_lambda=lambda x: x,
            not_found_error_lambda=lambda: ValueError(
                "Did not find any matching channel hierarchy that would fit for that frame number! {}".format(frame_number))
        )
