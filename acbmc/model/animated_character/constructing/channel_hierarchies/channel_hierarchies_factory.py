from typing import Dict
from acbmc.model.animated_character.constructing.channel_hierarchies.channel_hierarchy_factory import ChannelHierarchyFactory
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies


class ChannelHierarchiesFactory:
    def construct_from_json_dict(self, channel_hierarchies_json_dict) -> ChannelHierarchies:
        result = ChannelHierarchies()
        result.channel_hierarchies = self._get_channel_hierarchies(channel_hierarchies_json_dict["channelHierarchies"])
        return result

    def _get_channel_hierarchies(self, channel_hierarchies_json_dict) -> Dict[str, ChannelHierarchy]:
        result = dict()  # type: Dict[str, ChannelHierarchy]
        channel_hierarchy_factory = ChannelHierarchyFactory()
        for channel_hierarchy_identifier in channel_hierarchies_json_dict:
            result[channel_hierarchy_identifier] = channel_hierarchy_factory.construct_from_json_dict(
                channel_hierarchies_json_dict[channel_hierarchy_identifier])
        return result
        