from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.subobjects_library import SubobjectsLibrary
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.animation_clips import AnimationClips


class AnimatedCharacterDescriptionBuilder:
    def __init__(self):
        self.result = AnimatedCharacterDescription()

    def set_name(self, name: str) -> 'AnimatedCharacterDescriptionBuilder':
        self.result.name = name
        return self

    def set_animation_clips(self, animation_clips: AnimationClips) -> 'AnimatedCharacterDescriptionBuilder':
        self.result.animation_clips = animation_clips
        return self

    def set_subobjects_library(self, subobjects_library: SubobjectsLibrary) -> 'AnimatedCharacterDescriptionBuilder':
        self.result.subobjects_library = subobjects_library
        return self

    def set_channel_hierarchies(self, channel_hierarchies: ChannelHierarchies) -> 'AnimatedCharacterDescriptionBuilder':
        self.result.channel_hierarchies = channel_hierarchies
        return self

    def set_subobjects_channels_associations(self, subobjects_channels_associations: SubobjectsChannelsAssociations) -> 'AnimatedCharacterDescriptionBuilder':
        self.result.subobjects_channels_associations = subobjects_channels_associations
        return self

    def build(self) -> AnimatedCharacterDescription:
        return self.result
