from typing import Dict, List
from acbmc.model.animated_character.model.subobjects_channels_associations_desc.subobjects_channels_association import \
 SubobjectsChannelsAssociation, SubobjectsChannelsAssociationDescription


class SubobjectsChannelsAssociationDescriptionFactory:
    def construct_from_json_dict(self, subobjects_channels_associations_description_json_dict) -> SubobjectsChannelsAssociationDescription:
        result = SubobjectsChannelsAssociationDescription()
        result.channels_for_subobjects_parenting = self._get_channels_for_subobjects_parenting(
            subobjects_channels_associations_description_json_dict["channelsForSubobjectsParenting"])
        result.channels_for_subobjects_bones_parenting = self._get_channels_for_subobjects_bones_parenting(
            subobjects_channels_associations_description_json_dict["channelsForSubobjectsBonesParenting"]
        )
        return result

    def _get_channels_for_subobjects_parenting(self, channels_for_subobjects_parenting_json_dict) -> Dict[int, List[int]]:
        return {int(key):[int(x) for x in value_list] for (key,value_list) in channels_for_subobjects_parenting_json_dict.items()}

    def _get_channels_for_subobjects_bones_parenting(self, channels_for_subobjects_bones_parenting_json_dict) -> Dict[int, Dict[int, List[int]]]:
        return {int(outer_key):{int(inner_key):[int(x) for x in inner_list] for (inner_key,inner_list) in outer_value.items()} for (outer_key,outer_value)
         in channels_for_subobjects_bones_parenting_json_dict.items()}


class SubobjectsChannelsAssociationFactory:
    def construct_from_json_dict(self, subobjects_channels_association_json_dict) -> SubobjectsChannelsAssociation:
        result = SubobjectsChannelsAssociation()
        result.subobjects_channels_association_identifier = subobjects_channels_association_json_dict["subobjectsChannelsAssociationIdentifier"]
        result.subobjects_channels_associations_description = SubobjectsChannelsAssociationDescriptionFactory(). \
            construct_from_json_dict(subobjects_channels_association_json_dict["subobjectsChannelsAssociationsDescription"])
        return result
