from acbmc.util.model.tree_hierarchy import TreeHierarchy
from typing import List, Union
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model \
    .subobjects_channels_associations_desc.subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChannelBoneHierarchyInfoNode:
    def __init__(self):
        self.channel_id = -1  # type: int

    
class EndBoneHierarchySubobjectInfoNode:
    def __init__(self):
        self.subobject_number = -1  # type: int
        self.has_bones = False  # type: bool


class FlattenedArmatureHierarchyHelper:
    @classmethod
    def _get_bones_hierarchy_info_related_to_channel(
        cls,
        channel_id: int,
        channel_hierarchy: ChannelHierarchy,
        channels_for_subobjects_association: SubobjectsChannelsAssociation
    ) -> TreeHierarchy:

        channel_parents_ids_chain_list_in_parenting_descending_order = \
            ChannelHierarchyHelper.get_channel_parents_ids_chain_list_in_parenting_descending_order(
                channel_id, channel_hierarchy
            )

        channel_

        
        raise NotImplementedError

    @classmethod
    def _get_subobject_id_related_to_channel_parenting_chain_for(
        cls,
        channel_id: int,
        channel_hierarchy: ChannelHierarchy,
        channels_for_subobjects_association: SubobjectsChannelsAssociation
    ) -> int:

        bones_chain_related_to_channel = cls._get_bones_chain_info_related_to_channel(channel_id, channel_hierarchy, channels_for_subobjects_association)
        raise NotImplementedError

    @classmethod
    def _is_resulting_bone_actual_bone_of_subobject_or_not__then_object_parenting_mocking_bone(
        cls,
        channel_id: int,
        channel_hierarchy: ChannelHierarchy,
        channels_for_subobjects_association: SubobjectsChannelsAssociation
    ) -> bool:

        bones_chain_related_to_channel = cls._get_bones_chain_info_related_to_channel(channel_id)
        raise NotImplementedError

    @classmethod
    def _get_proper_subobject_bone_index_for(
        cls,
        channel_id: int,
        channel_hierarchy: ChannelHierarchy,
        channels_for_subobjects_association: SubobjectsChannelsAssociation
    ) -> int:

        bones_chain_related_to_channel = cls._get_bones_chain_info_related_to_channel(channel_id)
        raise NotImplementedError

    @classmethod
    def get_bone_names_qualified_for_keyframing_in_flattened_hierarchy(
        cls,
        channel_id: int,
        channel_hierarchy: ChannelHierarchy,
        channels_for_subobjects_association: SubobjectsChannelsAssociation) -> List[str]:

        bones_hierarchy_related_to_channel = \
            cls._get_bones_hierarchy_info_related_to_channel(channel_id, channel_hierarchy, channels_for_subobjects_association)
        """
        subobject_id = cls._get_subobject_id_related_to_channel_parenting_chain_for(
            channel_id, channel_hierarchy, channels_for_subobjects_association)  
        has_bones = cls._is_resulting_bone_actual_bone_of_subobject_or_not__then_object_parenting_mocking_bone(
            channel_id, channel_hierarchy, channels_for_subobjects_association
        )

        if has_bones:
            subobject_bone_index = cls._get_proper_subobject_bone_index_for(channel_id, channel_hierarchy, channels_for_subobjects_association) 
            result_bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for(
                bone_in_subobject_index=subobject_bone_index, subobject_number=subobject_id)
        else:
            result_bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_mock_bone_name_for_object_parenting(subobject_id)

        return result_bone_name
        """