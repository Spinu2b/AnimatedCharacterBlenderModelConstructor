from acbmc.model.animated_character.constructing.subobjects_channels_associations.subobjects_channels_associations_factory import SubobjectsChannelsAssociationsFactory
from acbmc.model.animated_character.constructing.channel_hierarchies.channel_hierarchies_factory import ChannelHierarchiesFactory
from acbmc.model.animated_character.constructing.subobjects_library.subobjects_library_factory import SubobjectsLibraryFactory
from acbmc.model.animated_character.constructing.animation_clips.animation_clips_factory import AnimationClipsFactory
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library import SubobjectsLibrary
from acbmc.model.animated_character.model.animation_clips import AnimationClips
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.animated_character.constructing.animated_character_description_builder import AnimatedCharacterDescriptionBuilder


class AnimatedCharacterDescriptionJsonDictHelper:
    def get_name(self, animated_character_json_dict) -> str:
        return animated_character_json_dict["name"]

    def get_animation_clips_obj(self, animated_character_json_dict) -> AnimationClips:
        return AnimationClipsFactory().construct_from_json_dict(animated_character_json_dict["animationClips"])

    def get_subobjects_library_obj(self, animated_character_json_dict) -> SubobjectsLibrary:
        return SubobjectsLibraryFactory().construct_from_json_dict(animated_character_json_dict["subobjectsLibrary"])

    def get_channel_hierarchies_obj(self, animated_character_json_dict) -> ChannelHierarchies:
        return ChannelHierarchiesFactory().construct_from_json_dict(animated_character_json_dict["channelHierarchies"])

    def get_subobjects_channels_associations_obj(self, animated_character_json_dict) -> SubobjectsChannelsAssociations:
        return SubobjectsChannelsAssociationsFactory().construct_from_json_dict(animated_character_json_dict["subobjectsChannelsAssociations"])


class AnimatedCharacterDescriptionFactory:
    def construct_from_json(self, animated_character_json_dict) -> AnimatedCharacterDescription:
        result_builder = AnimatedCharacterDescriptionBuilder()
        animated_character_description_json_dict_helper = AnimatedCharacterDescriptionJsonDictHelper()
        
        result_builder.set_name(animated_character_description_json_dict_helper.get_name(animated_character_json_dict))
        result_builder.set_animation_clips(
            animated_character_description_json_dict_helper.get_animation_clips_obj(animated_character_json_dict))
        result_builder.set_subobjects_library(
            animated_character_description_json_dict_helper.get_subobjects_library_obj(animated_character_json_dict))
        result_builder.set_channel_hierarchies(
            animated_character_description_json_dict_helper.get_channel_hierarchies_obj(animated_character_json_dict))
        result_builder.set_subobjects_channels_associations(
            animated_character_description_json_dict_helper.get_subobjects_channels_associations_obj(animated_character_json_dict))
        return result_builder.build()
