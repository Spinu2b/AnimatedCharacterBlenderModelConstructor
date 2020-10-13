from typing import Dict, Iterator, List, Set
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class ArmatureTreeHierarchiesIteratingHelper:
    def iterate_armature_hierarchies_for(
        self,
        frames_count: int,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: Dict[str, ChannelHierarchy],
        channel_keyframes: Dict[int, Dict[int, ChannelTransform]],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation],
        channels_for_subobjects_associations_data: Dict[str, List[AnimationFramesPeriodInfo]],
        animation_hierarchies: Dict[str, List[AnimationFramesPeriodInfo]]
    ) -> Iterator[ArmatureTreeHierarchy]:
        first_frame_number = 1
        previous_channels_set = \
            self._get_channels_set_for_frame(
                frame_number=first_frame_number,
                animation_hierarchies=animation_hierarchies,
                channel_hierarchies=channel_hierarchies)  # type: Set[int]

        previous_channel_transforms = self._get_channel_transforms_for_frame(
            frame_number=first_frame_number,
            channel_keyframes=channel_keyframes)  # Dict[int, ChannelTransform]

        previous_channels_for_subobjects_association = \
            self._get_channels_for_subobjects_associations_data_for_frame(
                frame_number=first_frame_number,
                channels_for_subobjects_associations_data=channels_for_subobjects_associations_data,
                subobjects_channels_associations=subobjects_channels_associations)  # type: SubobjectsChannelsAssociation

        previous_channel_hierarchy = self._get_channel_hierarchy_for_frame(
            frame_number=first_frame_number,
            animation_hierarchies=animation_hierarchies,
            channel_hierarchies=channel_hierarchies)  # type: ChannelHierarchy

        for frame_number in range(1, frames_count+1):
            current_channels_set = self._get_channels_set_for_frame(
                frame_number=frame_number,
                animation_hierarchies=animation_hierarchies,
                channel_hierarchies=channel_hierarchies)  # type: Set[int]

            current_channel_transforms = self._get_channel_transforms_for_frame(
                frame_number=frame_number,
                channel_keyframes=channel_keyframes)  # type: Dict[int, ChannelTransform]    

            current_channels_for_subobjects_association = \
                self._get_channels_for_subobjects_association_for_frame(
                    frame_number=frame_number,
                    channels_for_subobjects_associations_data=channels_for_subobjects_associations_data,
                    subobjects_channels_associations=subobjects_channels_associations)  # type: SubobjectsChannelsAssociation

            current_channel_hierarchy = self._get_channel_hierarchy_for_frame(
                frame_number=frame_number,
                animation_hierarchies=animation_hierarchies,
                channel_hierarchies=channel_hierarchies)  # type: ChannelHierarchy

            # If channels set changed between frames
            # OR
            # If channels to subobjects associations changed between frames
            # OR
            # If channels hierarchy changed between frames
            # THEN
            # Get new armature hierarchy that reflects that change
            if not AnimationClipDataComparisonHelper.are_channel_sets_equal(previous_channels_set, current_channels_set) or \
                not AnimationClipDataComparisonHelper.are_channels_for_subobjects_associations_equal(
                    previous_channels_for_subobjects_association, current_channels_for_subobjects_association) or \
                        not AnimationClipDataComparisonHelper.are_channel_hierarchies_equal(previous_channel_hierarchy, current_channel_hierarchy):
                        yield self._derive_armature_tree_hierarchy_for(
                            channel_hierarchy=current_channel_hierarchy,
                            channels_set=current_channels_set,
                            channel_tranforms=current_channel_transforms,
                            channels_for_subobjects_association=current_channels_for_subobjects_association,
                            subobjects_dict=subobjects_dict)

            previous_channel_hierarchy = current_channel_hierarchy
            previous_channel_transforms = current_channel_transforms
            previous_channels_for_subobjects_association = current_channels_for_subobjects_association
            previous_channels_set = current_channels_set

        raise NotImplementedError            


class UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher:
    def iterate_armature_hierarchies_with_deform_sets_for_animation_clip(
        self,
        animation_clip: AnimationClip,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: ChannelHierarchies,
        subobjects_channels_associations: SubobjectsChannelsAssociations) -> Iterator[ArmatureTreeHierarchy]:
        raise NotImplementedError
