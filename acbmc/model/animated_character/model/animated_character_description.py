from acbmc.model.animated_character.model.subobjects_library import SubobjectsLibrary
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.animation_clips import AnimationClips


class AnimatedCharacterDescription:
    def __init__(self):
        self.name = None  # type: str
        self.subobjects_library = SubobjectsLibrary()
        self.channel_hierarchies = ChannelHierarchies()
        self.subobjects_channels_associations = SubobjectsChannelsAssociations()
        self.animation_clips = AnimationClips()
