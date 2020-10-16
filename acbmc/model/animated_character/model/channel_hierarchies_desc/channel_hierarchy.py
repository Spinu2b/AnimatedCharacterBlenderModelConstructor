from typing import Dict, Set


class ChannelHierarchyDescription:
    def __init__(self):
        self.channels = set()  # type: Set[int]
        self.parenting = dict()  # type: Dict[int, int]


class ChannelHierarchy:
    def __init__(self):
        self.channel_hierarchy_description_identifier = None  # type: str
        self.channel_hierarchy = ChannelHierarchyDescription()
