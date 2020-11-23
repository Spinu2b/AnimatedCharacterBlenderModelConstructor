from typing import Dict, Set
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode


class UnifiedChannelsArmatureTreeHierarchyWithDeformSetsHelper:
    @staticmethod
    def associate_channels_armature_tree_hierarchy_with_deform_sets(
        channels_set: Set[int],
        channels_armature_tree_hierarchy: TreeHierarchy,
        channels_with_appropriate_subobjects_deform_sets_associations: Dict[int, Dict[str, BoneAbsoluteTransformNode]]
    ):
        for with_deform_set_associated_channel_id \
            in channels_with_appropriate_subobjects_deform_sets_associations:
            for deform_set_associated_to_channel_bone_name in \
                 channels_with_appropriate_subobjects_deform_sets_associations[with_deform_set_associated_channel_id]:
                 channels_armature_tree_hierarchy.add_node(
                     parent_key=UnifiedArmatureWithDeformSetsBonesNamingHelper
                        .get_bone_name_for_channel_id(channel_id=with_deform_set_associated_channel_id),
                     node_key=deform_set_associated_to_channel_bone_name,
                     node=channels_with_appropriate_subobjects_deform_sets_associations
                        [with_deform_set_associated_channel_id][deform_set_associated_to_channel_bone_name])
