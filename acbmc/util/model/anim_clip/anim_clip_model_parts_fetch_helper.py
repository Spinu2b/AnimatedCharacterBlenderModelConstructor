from typing import Any, Callable, Dict, List, Set, Tuple
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChannelTransformInterpolationHelper:
    @classmethod
    def _get_preeceding_keyframe_key_appropriate_for_frame_number(
        cls, frame_number: int, frames_count: int, channel_timeline_keyframes: Dict[int, ChannelTransform]
    ) -> int:
        return [keyframe_key for keyframe_key in sorted(channel_timeline_keyframes) if keyframe_key <= frame_number][-1]


    @classmethod
    def _is_end_keyframe(cls, keyframe_key: int, channel_timeline_keyframes: Dict[int, ChannelTransform]) -> bool:
        return keyframe_key >= max(channel_timeline_keyframes)

    @classmethod
    def _get_first_keyframe_key(cls, channel_timeline_keyframes: Dict[int, ChannelTransform]) -> int:
        return min(channel_timeline_keyframes)

    @classmethod
    def _get_next_keyframe_key_after(cls, keyframe_key: int, channel_timeline_keyframes: Dict[int, ChannelTransform]) -> int:
        if cls._is_end_keyframe(keyframe_key=keyframe_key, channel_timeline_keyframes=channel_timeline_keyframes):
            return cls._get_first_keyframe_key(channel_timeline_keyframes=channel_timeline_keyframes)
        else:
            return [key for key in sorted(channel_timeline_keyframes) if key > keyframe_key][0]

    @classmethod
    def interpolate_linear_for_frame(cls, frame_number: int, frames_count: int,
        channel_timeline_keyframes: Dict[int, ChannelTransform]) -> ChannelTransform:
        preceeding_keyframe_key_appropriate_for_frame_number = \
            cls._get_preeceding_keyframe_key_appropriate_for_frame_number(
                frame_number=frame_number,
                frames_count=frames_count,
                channel_timeline_keyframes=channel_timeline_keyframes)  # type: int

        frames_since_keyframe = frame_number - preceeding_keyframe_key_appropriate_for_frame_number  # type: int

        if cls._is_end_keyframe(preceeding_keyframe_key_appropriate_for_frame_number, channel_timeline_keyframes):
            next_keyframe_key = cls._get_first_keyframe_key(channel_timeline_keyframes)  # type: int
            frames_difference = frames_count - 1 + next_keyframe_key - preceeding_keyframe_key_appropriate_for_frame_number  # type: int
            if frames_difference == 0:
                interpolation = 0.0  # type: float
            else:
                interpolation = frames_since_keyframe / float(frames_difference)  # type: float
        else:
            next_keyframe_key = cls._get_next_keyframe_key_after(
                preceeding_keyframe_key_appropriate_for_frame_number,
                channel_timeline_keyframes)  # type: int

            frames_difference = next_keyframe_key - preceeding_keyframe_key_appropriate_for_frame_number  # type: int
            interpolation = frames_since_keyframe / float(frames_difference)  # type: float

        keyframe_channel_transform_a = channel_timeline_keyframes[preceeding_keyframe_key_appropriate_for_frame_number]  # type: ChannelTransform
        keyframe_channel_transform_b = channel_timeline_keyframes[next_keyframe_key]  # type: ChannelTransform

        return ChannelTransform.lerp(keyframe_channel_transform_a, keyframe_channel_transform_b, interpolation)


class AnimationFramesPeriodedAnimClipDataHelper:
    def find_matching_store_data(
        frame_number: int,  
        animation_clip_frames_periods_data: Dict[str, List[AnimationFramesPeriodInfo]],
        string_identifiable_data_store: Dict[str, Any],
        match_return_lambda: Callable[[Any], Any],
        not_found_error_lambda: Callable[[], Any]) -> Any:
        for data_store_part_identifier, animation_frames_period_infos_list in animation_clip_frames_periods_data.items():
            if any(x.contains_frame_number(frame_number) for x in animation_frames_period_infos_list):
                return match_return_lambda(string_identifiable_data_store[data_store_part_identifier])
        raise not_found_error_lambda()        
    

class AnimationClipModelPartsFetchingHelper:
    @staticmethod
    def get_channels_set_for_frame(
        frame_number: int,
        channel_keyframes: Dict[int, Dict[int, ChannelTransform]]) -> Set[int]:

        return set(channel_keyframes.keys())
        # return AnimationFramesPeriodedAnimClipDataHelper.find_matching_store_data(
        #    frame_number=frame_number,
        #     animation_clip_frames_periods_data=animation_hierarchies,
        #    string_identifiable_data_store=channel_hierarchies,
        #    match_return_lambda=lambda x: x.channel_hierarchy.channels,
        #    not_found_error_lambda=lambda: ValueError(
        #        "Did not find any matching animation hierarchy that would fit for that frame number! {}".format(frame_number))
        #)

    @staticmethod
    def get_channel_transforms_for_frame(
        frame_number: int,
        frames_count: int,
        channel_keyframes: Dict[int, Dict[int, ChannelTransform]]) -> Dict[int, ChannelTransform]:
        
        result = dict()  # type: Dict[int, ChannelTransform]
        for channel_identifier in channel_keyframes:
            result[channel_identifier] = \
                ChannelTransformInterpolationHelper.interpolate_linear_for_frame(
                    frame_number=frame_number,
                    frames_count=frames_count,
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
