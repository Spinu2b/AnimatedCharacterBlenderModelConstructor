from acbmc.model.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.model.subobjects_library import SubobjectsLibrary
from acbmc.model.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.model.animation_clips import AnimationClips


class AnimatedCharacterDescriptionBuilder:
    def __init__(self):
        self.result = AnimatedCharacterDescription()

    def set_name(self, name: str) -> 'AnimatedCharacterDescriptionBuilder':
        self.result.name = name
        return self

    def set_animation_clips(self, animation_clips: AnimationClips) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def set_subobjects_library(self, subobjects_library: SubobjectsLibrary) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def set_channel_hierarchies(self, channel_hierarchies: ChannelHierarchies) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def set_subobjects_channels_associations(self, subobjects_channels_associations: SubobjectsChannelsAssociations) -> 'AnimatedCharacterDescriptionBuilder':
        raise NotImplementedError
        return self

    def build(self) -> AnimatedCharacterDescription:
        raise NotImplementedError
