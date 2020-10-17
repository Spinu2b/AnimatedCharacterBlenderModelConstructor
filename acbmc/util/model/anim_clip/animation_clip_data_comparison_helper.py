from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from typing import Set


class AnimationClipDataComparisonHelper:
    @staticmethod
    def are_channel_sets_equal(channels_set_a: Set[int], channels_set_b: Set[int]) -> bool:
        raise NotImplementedError

    @staticmethod
    def are_channels_for_subobjects_associations_equal(
        channels_for_subobjects_association_a: SubobjectsChannelsAssociation,
        channels_for_subobjects_association_b: SubobjectsChannelsAssociation) -> bool:
        raise NotImplementedError

    @staticmethod
    def are_channel_hierarchies_equal(
        channel_hierarchy_a: ChannelHierarchy,
        channel_hierarchy_b: ChannelHierarchy
    ) -> bool:
        raise NotImplementedError
