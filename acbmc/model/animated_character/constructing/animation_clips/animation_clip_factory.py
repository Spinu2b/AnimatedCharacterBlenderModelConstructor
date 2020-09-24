
from acbmc.model.animated_character.constructing.animation_clips.subobject_used_morph_association_info_morph_factory import SubobjectUsedMorphAssociationInfoMorphFactory
from acbmc.model.animated_character.constructing.animation_clips.animation_hierarchies_factory import AnimationHierarchiesFactory
from acbmc.model.animated_character.constructing.animation_clips.channels_for_subobjects_associations_data_factory import ChannelsForSubobjectsAssociationsDataFactory
from acbmc.model.animated_character.constructing.animation_clips.channel_keyframes_factory import ChannelKeyframesFactory
from acbmc.model.animated_character.model.animation_clips_desc.subobject_used_morph_association_info import SubobjectUsedMorphAssociationInfo
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class AnimationClipFactory:
    def construct_from_json_dict(self, animation_clip_json_dict) -> AnimationClip:
        result = AnimationClip()
        result.id = int(animation_clip_json_dict["id"])
        result.channel_keyframes = ChannelKeyframesFactory().construct_from_json_dict(animation_clip_json_dict["channelKeyframes"])
        result.channels_for_subobjects_associations_data = \
            ChannelsForSubobjectsAssociationsDataFactory().construct_from_json_dict(animation_clip_json_dict["channelsForSubobjectsAssociationsData"])
        result.animation_hierarchies = AnimationHierarchiesFactory().construct_from_json_dict(animation_clip_json_dict["animationHierarchies"])
        result.morphs = SubobjectUsedMorphAssociationInfoMorphFactory().construct_from_json_dict(animation_clip_json_dict["morphs"])    
        return result
