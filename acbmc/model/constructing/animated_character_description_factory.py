from acbmc.model.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.model.subobjects_library import SubobjectsLibrary
from acbmc.model.model.animation_clips import AnimationClips
from acbmc.model.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.constructing.animated_character_description_builder import AnimatedCharacterDescriptionBuilder


class AnimatedCharacterDescriptionJsonDictHelper:
    def get_animation_clips_obj(self, animated_character_json_dict) -> AnimationClips:
        raise NotImplementedError

    def get_subobjects_library_obj(self, animated_character_json_dict) -> SubobjectsLibrary:
        raise NotImplementedError

    def get_channel_hierarchies_obj(self, animated_character_json_dict) -> ChannelHierarchies:
        raise NotImplementedError

    def get_subobjects_channels_associations_obj(self, animated_character_json_dict) -> SubobjectsChannelsAssociations:
        raise NotImplementedError


class AnimatedCharacterDescriptionFactory:
    def construct_from_json(self, animated_character_json_dict) -> AnimatedCharacterDescription:
        result_builder = AnimatedCharacterDescriptionBuilder()
        animated_character_description_json_dict_helper = AnimatedCharacterDescriptionJsonDictHelper()
        
        result_builder.set_animation_clips(
            animated_character_description_json_dict_helper.get_animation_clips_obj(animated_character_json_dict))
        result_builder.set_subobjects_library(
            animated_character_description_json_dict_helper.get_subobjects_library_obj(animated_character_json_dict))
        result_builder.set_channel_hierarchies(
            animated_character_description_json_dict_helper.get_channel_hierarchies_obj(animated_character_json_dict))
        result_builder.set_subobjects_channels_associations(
            animated_character_description_json_dict_helper.get_subobjects_channels_associations_obj(animated_character_json_dict))
        return result_builder.build()
