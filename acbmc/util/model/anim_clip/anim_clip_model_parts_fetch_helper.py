from typing import Dict, List, Set
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class AnimationClipModelPartsFetchingHelper:
    @staticmethod
    def get_channels_set_for_frame(
        frame_number: int,
        animation_hierarchies: Dict[str, List[AnimationFramesPeriodInfo]],
        channel_hierarchies: Dict[str, ChannelHierarchy]) -> Set[int]:
        for channel_hierarchy_identifier, animation_frames_period_infos_list in animation_hierarchies.items():
            if any(x.contains_frame_number(frame_number) for x in animation_frames_period_infos_list):
                return channel_hierarchies[channel_hierarchy_identifier].channel_hierarchy.channels
        raise ValueError("Did not find any matching animation hierarchy that would fit for that frame number! {}".format(frame_number))

    @staticmethod
    def get_channel_transforms_for_frame(
        self, 
        frame_number: int,
        channel_keyframes: Dict[int, Dict[int, ChannelTransform]]) -> Dict[int, ChannelTransform]:
        raise NotImplementedError

    @staticmethod    
    def get_channels_for_subobjects_association_for_frame(
        self, 
        frame_number: int,
        channels_for_subobjects_associations_data: Dict[str, List[AnimationFramesPeriodInfo]],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation]) -> SubobjectsChannelsAssociation:
        raise NotImplementedError

    @staticmethod    
    def get_channel_hierarchy_for_frame(
        self,
        frame_number: int,
        animation_hierarchies: Dict[str, List[AnimationFramesPeriodInfo]],
        channel_hierarchies: Dict[str, ChannelHierarchy]) -> ChannelHierarchy:
        raise NotImplementedError
