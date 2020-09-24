from typing import Dict
from acbmc.model.animated_character.constructing.subobjects_channels_associations.subobjects_channels_association_factory import SubobjectsChannelsAssociationFactory
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations


class SubobjectsChannelsAssociationsFactory:
    def construct_from_json_dict(self, subobjects_channels_associations_json_dict) -> SubobjectsChannelsAssociations:
        result = SubobjectsChannelsAssociations()
        result.subobjects_channels_associations = self._get_subobjects_channels_associations(
            subobjects_channels_associations_json_dict["subobjectsChannelsAssociations"])
        return result

    def _get_subobjects_channels_associations(self, subobjects_channels_associations_json_dict) -> Dict[str, SubobjectsChannelsAssociation]:
        result = dict()  # type: Dict[str, SubobjectsChannelsAssociation]
        subobjects_channels_association_factory = SubobjectsChannelsAssociationFactory()
        for subobjects_channels_associations_identifier in subobjects_channels_associations_json_dict:
            result[subobjects_channels_associations_identifier] = \
                subobjects_channels_association_factory.construct_from_json_dict(
                    subobjects_channels_associations_json_dict[subobjects_channels_associations_identifier])
        return result
