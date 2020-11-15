from acbmc.model.blender.model.armature.bone_absolute_transform_node import BoneAbsoluteTransformNode
from typing import Iterator, Tuple
from acbmc.model.blender.model.armature.armature_bind_pose_model import ArmatureBindPoseModel
from acbmc.model.blender.model.armature.armature_tree_hierarchy import ArmatureTreeHierarchy


class ArmatureBindPoseConsolidationHelper:
    @classmethod
    def iterate_non_present_tree_nodes_prepared_for_bind_pose_model_building(
        cls,
        armature_tree_hierarchy_to_consolidate_with: ArmatureTreeHierarchy,
        result_armature_bind_pose_model: ArmatureBindPoseModel
    ) -> Iterator[Tuple[str, BoneAbsoluteTransformNode]]:
        raise NotImplementedError


class UnifiedArtistConvenientDeformSetsArmatureBindPoseBuilder:
    def __init__(self):
        self._result = ArmatureBindPoseModel()

    def consider_armature_hierarchy_with_deform_sets(
        self, armature_tree_hierarchy: ArmatureTreeHierarchy) -> 'UnifiedArtistConvenientDeformSetsArmatureBindPoseBuilder':

        for new_prepared_armature_tree_node in ArmatureBindPoseConsolidationHelper \
            .iterate_non_present_tree_nodes_prepared_for_bind_pose_model_building(
                armature_tree_hierarchy, self._result
            ):
            self._result.add_node(
                parent_key=None, node_key=new_prepared_armature_tree_node[0],
                node=new_prepared_armature_tree_node[1])

        """
        for new_channel_node in ArmatureBindPoseConsolidationHelper.iterate_non_present_channel_nodes(
            armature_tree_hierarchy, self._result,
        ):
            self._result.add_node(
                parent_key=None, node_key=new_channel_node.key, node=new_channel_node.copy())

        for new_deform_set_node in ArmatureBindPoseConsolidationHelper.iterate_non_present_deform_sets_nodes(
            armature_tree_hierarchy, self._result
        ):
            self._result.add_node(
                parent_key=None, node_key=new_channel_node.key, node=new_channel_node.copy())
        """        
        return self

    def build(self) -> ArmatureBindPoseModel:
        return self._result
