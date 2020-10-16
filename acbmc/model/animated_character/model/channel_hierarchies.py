from typing import Dict
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChannelHierarchies:
    def __init__(self):
        self.channel_hierarchies = dict()  # type: Dict[str, ChannelHierarchy]
