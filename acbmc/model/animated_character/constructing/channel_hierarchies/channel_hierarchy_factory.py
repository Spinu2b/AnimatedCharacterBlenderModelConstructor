from typing import Dict, Set
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy, ChannelHierarchyDescription


class ChannelHierarchyDescriptionFactory:
    def construct_from_json_dict(self, channel_hierarchy_description_json_dict) -> ChannelHierarchyDescription:
        result = ChannelHierarchyDescription()
        result.channels = self._get_channels(channel_hierarchy_description_json_dict["channels"])
        result.parenting = self._get_parenting(channel_hierarchy_description_json_dict["parenting"])
        return result

    def _get_channels(self, channels_json_dict) -> Set[int]:
        return {x for x in channels_json_dict}

    def _get_parenting(self, parenting_json_dict) -> Dict[int, int]:
        return {k:v for (k,v) in parenting_json_dict.items()}
        


class ChannelHierarchyFactory:
    def construct_from_json_dict(self, channel_hierarchy_json_dict) -> ChannelHierarchy:
        result = ChannelHierarchy()
        result.channel_hierarchy_description_identifier = channel_hierarchy_json_dict["channelHierarchyDescriptionIdentifier"]
        result.channel_hierarchy = ChannelHierarchyDescriptionFactory().construct_from_json_dict(channel_hierarchy_json_dict["channelHierarchy"])
        return result
