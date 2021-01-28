from typing import Callable, Dict, List, Optional, Set
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.uni_arm_tree_hierarch_to_only_def_set_bones_flat \
    import UnifiedArmatureTreeHierarchyToOnlyDeformSetBonesFlattener
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.uni_arm_tree_hierarch_help import UnifiedArmatureTreeHierarchyHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature \
    .channels.uni_chan_arm_tree_hierarch_with_def_sets_help import UnifiedChannelsArmatureTreeHierarchyWithDeformSetsHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature \
    .channels.uni_chan_arm_tree_hierarch_fact import UnifiedChannelsArmatureTreeHierarchyFactory
from acbmc.model.blender.constructing.bone_transform_node_factory import BoneTransformNodeFactory
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.dict_utils import DictUtils
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.subobjects_channels_associations_desc \
    .subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class UnifiedArmatureHierarchyChannelsToDeformSetsDataFetchingHelper:
    @classmethod
    def _get_bind_bone_poses_as_final_armature_bones_transforms_associated_to_channel(
        cls,
        channel_id: int,
        subobject_number: int,
        bind_bone_poses: Dict[int, TransformNode]
    ) -> Dict[str, BoneTransformNode]:
        
        result = dict()  # type: Dict[str, BoneTransformNode]
        for bone_in_subobject_index in bind_bone_poses:
            bone_name = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for(
                bone_in_subobject_index=bone_in_subobject_index,
                subobject_number=subobject_number)  # type: str

            result[bone_name] = BoneTransformNodeFactory.get_from_bind_bone_pose(
                bone_name=bone_name,
                bind_bone_pose=bind_bone_poses[bone_in_subobject_index])
        return result

    @classmethod
    def _get_bind_bone_pose_for_mock_bone_simulating_pure_channel_associated_object_parenting(
        cls,
        channel_id: int,
        subobject_number: int
    ) -> Dict[str, BoneTransformNode]:
        result = dict()

        mock_bone_name = \
            UnifiedArmatureWithDeformSetsBonesNamingHelper.get_mock_bone_name_for_object_parenting(
                subobject_number=subobject_number
            )

        mock_bone_transform_node = BoneTransformNode()  # use home transform, 0.0-kind position for given subobject
        mock_bone_transform_node.bone_name = mock_bone_name

        result[mock_bone_name] = mock_bone_transform_node
        return result

    @classmethod
    def get_channels_for_appropriate_subobjects_deform_sets_associations(
        cls,
        channels_set: Set[int],
        subobjects_dict: Dict[int, Subobject],
        channels_for_subobjects_parenting: Dict[int, List[int]],
        channels_for_subobjects_bones_parenting: Dict[int, Dict[int, List[int]]]
    ) -> Dict[int, Dict[str, BoneTransformNode]]:
        result = {channel_id: dict() for channel_id in channels_set}  # type: Dict[int, Dict[str, BoneTransformNode]]

        for channel_id in channels_set:
            if channel_id in channels_for_subobjects_bones_parenting:
                for subobject_number in channels_for_subobjects_bones_parenting[channel_id]:     
                    DictUtils.extend_dict_with_duplicated_keys_errors(
                        base_dict=result[channel_id],
                        extending_dict=
                        cls._get_bind_bone_poses_as_final_armature_bones_transforms_associated_to_channel(
                            channel_id=channel_id,
                            subobject_number=subobject_number,
                            bind_bone_poses=subobjects_dict[subobject_number].geometric_object.bind_bone_poses))

            if channel_id in channels_for_subobjects_parenting:
                for subobject_number in channels_for_subobjects_parenting[channel_id]:
                    DictUtils.extend_dict_with_duplicated_keys_errors(
                        base_dict=result[channel_id],
                        extending_dict=
                        cls._get_bind_bone_pose_for_mock_bone_simulating_pure_channel_associated_object_parenting(
                            channel_id=channel_id,
                            subobject_number=subobject_number
                        )
                    )

        return result


class UnifiedArmatureTreeHierarchyFactory:
    @classmethod
    def derive_armature_tree_hierarchy_for(
        cls,
        frame_number: int,
        channel_hierarchy: ChannelHierarchy,
        channels_set: Set[int],
        particular_frame_channel_transforms: Dict[int, TransformNode],
        channels_for_subobjects_association: SubobjectsChannelsAssociation,
        channel_keyframes: Dict[int, Dict[int, TransformNode]],
        subobjects_dict: Dict[int, Subobject],
        result_tree_hierarchy_transformation: Optional[Callable[[None], TreeHierarchy]]
    ) -> TreeHierarchy:
    
        channels_parenting = channel_hierarchy.channel_hierarchy.parenting  # type: Dict[int, int]
        channels_with_appropriate_subobjects_deform_sets_associations = \
            UnifiedArmatureHierarchyChannelsToDeformSetsDataFetchingHelper.get_channels_for_appropriate_subobjects_deform_sets_associations(
                channels_set=channels_set,
                subobjects_dict=subobjects_dict,
                channels_for_subobjects_parenting=channels_for_subobjects_association \
                 .subobjects_channels_associations_description.channels_for_subobjects_parenting,
                channels_for_subobjects_bones_parenting=channels_for_subobjects_association \
                 .subobjects_channels_associations_description.channels_for_subobjects_bones_parenting
            )  # type: Dict[int, Dict[str, BoneTransformNode]]   # These bone transforms should be indeed governing bones' home positions relative to their proper subobject
            # They will be later translated accordingly to channels governing them in that particular armature tree hierarchy
        
        result_armature_tree_hierarchy = \
            UnifiedChannelsArmatureTreeHierarchyFactory \
                .construct_pure_channels_armature_tree_hierarchy(
                    channels_set=channels_set,
                    channels_parenting=channels_parenting,
                    channel_transforms=particular_frame_channel_transforms
                )  # type: TreeHierarchy

        UnifiedChannelsArmatureTreeHierarchyWithDeformSetsHelper \
            .associate_channels_armature_tree_hierarchy_with_deform_sets(
                channels_set=channels_set,
                channels_armature_tree_hierarchy=result_armature_tree_hierarchy,
                channels_with_appropriate_subobjects_deform_sets_associations=
                    channels_with_appropriate_subobjects_deform_sets_associations
                )

        result_armature_tree_hierarchy = UnifiedArmatureTreeHierarchyToOnlyDeformSetBonesFlattener \
            .flatten_armature_to_using_only_deform_set_bones_using_channel_bones_transforms_parenting_chains(result_armature_tree_hierarchy) 

        UnifiedArmatureTreeHierarchyHelper.make_armature_tree_hierarchy_having_one_root(
            result_armature_tree_hierarchy
        )

        if result_tree_hierarchy_transformation is not None:
            result_armature_tree_hierarchy = \
                result_tree_hierarchy_transformation(
                    tree_hierarchy=result_armature_tree_hierarchy,
                    channel_keyframes=channel_keyframes,
                    frame_number=frame_number)

        return result_armature_tree_hierarchy
