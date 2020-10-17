from typing import Dict, List


class SubobjectsChannelsAssociationDescription:
    def __init__(self):
        self.channels_for_subobjects_parenting = dict()  # type: Dict[int, List[int]]
        self.channels_for_subobjects_bones_parenting = dict()  # type: Dict[int, Dict[int, List[int]]]


class SubobjectsChannelsAssociation:
    def __init__(self):
        self.subobjects_channels_association_identifier = None  # type: str
        self.subobjects_channels_association_description = SubobjectsChannelsAssociationDescription()
