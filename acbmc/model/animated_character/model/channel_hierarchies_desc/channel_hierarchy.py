from typing import Dict, Set
from acbmc.util.DictUtils import DictUtils
from acbmc.util.CollectionsUtils import CollectionsUtils


class ChannelHierarchyDescription:
    def __init__(self):
        self.channels = set()  # type: Set[int]
        self.parenting = dict()  # type: Dict[int, int]

    def equals(self, other: 'ChannelHierarchyDescription') -> bool:
        return CollectionsUtils.have_the_same_elements(
            self.channels, other.channels) and \
                DictUtils.are_dicts_equal(
                    dict_a=self.parenting,
                    dict_b=other.parenting,
                    value_comparison_lambda=
                        lambda value_a, value_b: value_a == value_b
                )


class ChannelHierarchy:
    def __init__(self):
        self.channel_hierarchy_description_identifier = None  # type: str
        self.channel_hierarchy = ChannelHierarchyDescription()

    def equals(self, other: 'ChannelHierarchy') -> bool:
        return self.channel_hierarchy_description_identifier == \
            other.channel_hierarchy_description_identifier and \
                self.channel_hierarchy.equals(other.channel_hierarchy)
