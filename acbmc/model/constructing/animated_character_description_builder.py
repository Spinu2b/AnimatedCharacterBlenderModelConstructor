from acbmc.model.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.model.subobjects_library import SubobjectsLibrary
from acbmc.model.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.model.animation_clips import AnimationClips


class AnimatedCharacterDescriptionBuilder:
    def set_animation_clips(animation_clips: AnimationClips) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def set_subobjects_library(subobjects_library: SubobjectsLibrary) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def set_channel_hierarchies(channel_hierarchies: ChannelHierarchies) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def set_subobjects_channels_associations(subobjects_channels_associations: SubobjectsChannelsAssociations) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def build(self) -> AnimatedCharacterDescription:
        raise NotImplementedError
