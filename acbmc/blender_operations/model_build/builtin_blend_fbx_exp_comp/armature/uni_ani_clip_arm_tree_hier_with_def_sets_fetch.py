from typing import Dict, Iterator
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher:
    def iterate_armature_hierarchies_with_deform_sets_for_animation_clip(
        self,
        animation_clip: AnimationClip,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: ChannelHierarchies,
        subobjects_channels_associations: SubobjectsChannelsAssociations) -> Iterator[ArmatureTreeHierarchy]:
        raise NotImplementedError
