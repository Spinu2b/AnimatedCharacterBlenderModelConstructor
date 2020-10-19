from typing import Dict, List
from acbmc.util.DictUtils import DictUtils
from acbmc.util.CollectionsUtils import CollectionsUtils


class SubobjectsChannelsAssociationDescriptionComparisonHelper:
    @staticmethod
    def are_channels_for_subobjects_parentings_equal(
        channels_for_subobjects_parenting_a: Dict[int, List[int]],
        channels_for_subobjects_parenting_b: Dict[int, List[int]]
    ) -> bool:
        return DictUtils.are_dicts_equal(
            dict_a=channels_for_subobjects_parenting_a,
            dict_b=channels_for_subobjects_parenting_b,
            value_comparison_lambda=
                lambda list_a, list_b:
                    CollectionsUtils.have_the_same_elements(
                        list_a, list_b
                    )
            )

    @staticmethod
    def are_channels_for_subobjects_bones_parentings_equal(
        channels_for_subobjects_bones_parenting_a: Dict[int, Dict[int, List[int]]],
        channels_for_subobjects_bones_parenting_b: Dict[int, Dict[int, List[int]]]
    ) -> bool:
        return DictUtils.are_dicts_equal(
            dict_a=channels_for_subobjects_bones_parenting_a,
            dict_b=channels_for_subobjects_bones_parenting_b,
            value_comparison_lambda= 
                lambda dict_a, dict_b: 
                    DictUtils.are_dicts_equal(
                        dict_a=dict_a,
                        dict_b=dict_b,
                        value_comparison_lambda=
                            lambda list_a, list_b:
                                CollectionsUtils.have_the_same_elements(list_a, list_b)
                    )
            )

class SubobjectsChannelsAssociationDescription:
    def __init__(self):
        self.channels_for_subobjects_parenting = dict()  # type: Dict[int, List[int]]
        self.channels_for_subobjects_bones_parenting = dict()  # type: Dict[int, Dict[int, List[int]]]

    def equals(self, other: 'SubobjectsChannelsAssociationDescription') -> bool:
        return SubobjectsChannelsAssociationDescriptionComparisonHelper \
            .are_channels_for_subobjects_parentings_equal(
                self.channels_for_subobjects_parenting,
                other.channels_for_subobjects_parenting
            ) and \
                SubobjectsChannelsAssociationDescriptionComparisonHelper \
                    .are_channels_for_subobjects_bones_parentings_equal(
                        self.channels_for_subobjects_bones_parenting,
                        other.channels_for_subobjects_bones_parenting
                    )


class SubobjectsChannelsAssociation:
    def __init__(self):
        self.subobjects_channels_association_identifier = None  # type: str
        self.subobjects_channels_associations_description = SubobjectsChannelsAssociationDescription()

    def equals(self, other: 'SubobjectsChannelsAssociation') -> bool:
        return self.subobjects_channels_association_identifier \
            == other.subobjects_channels_association_identifier and \
                self.subobjects_channels_associations_description.equals(other.subobjects_channels_associations_description)
