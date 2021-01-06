from typing import Callable
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d
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

    def reform_space_model(
        self,
        position3d_transformation: Callable[[Vector3d], None],
        rotation_transformation: Callable[[Quaternion], None]):
        
        self.subobjects_library.reform_space_model(
            position3d_transformation=position3d_transformation, rotation_transformation=rotation_transformation)
        self.animation_clips.reform_space_model(
            position3d_transformation=position3d_transformation, rotation_transformation=rotation_transformation
        )
