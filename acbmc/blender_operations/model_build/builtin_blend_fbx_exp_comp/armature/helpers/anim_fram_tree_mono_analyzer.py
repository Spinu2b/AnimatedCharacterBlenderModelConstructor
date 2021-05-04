import copy
from typing import Dict, List
from acbmc.util.float_comparison_helper import FloatComparisonHelper
from acbmc.util.model.transform_node import TransformNode
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class TreeHierarchiesAnalysisConsolidationHelper:
    @classmethod
    def get_corresponding_bones_name_keyframes_in_trees(
        cls, tree_a: TreeHierarchy, tree_b: TreeHierarchy) -> List[str]:
        result = []  # type: List[str]
    
        for node_iter in tree_a.iterate_nodes():
            if tree_b.contains_node_key(key=node_iter.key):
                result.append(node_iter.key)

        return result

class TransformAnalysisHelper:
    @classmethod
    def calculate_transforms_discrepancy(
        cls, transform_a: TransformNode, transform_b: TransformNode) -> float:
        position_discrepancy = (transform_a.position - transform_b.position).magnitude()
        scale_discrepancy = (transform_a.scale - transform_b.scale).magnitude()

        return position_discrepancy + scale_discrepancy


class AnimationFramesTreesMonotonnyAnalyzer:
    def __init__(self):
        self.trees = []  # type: List[TreeHierarchy]

    def consider_tree(self, tree_hierarchy: TreeHierarchy):
        self.trees.append(copy.deepcopy(tree_hierarchy))

    def raise_exception_if_monotonous(self):
        result = dict()  # type: Dict[str, float]

        for tree_index in range(len(self.trees) - 1):
            for bone_name in \
                TreeHierarchiesAnalysisConsolidationHelper.get_corresponding_bones_name_keyframes_in_trees(
                    self.trees[tree_index], self.trees[tree_index + 1]):
                if bone_name not in result:
                    result[bone_name] = 0.0
                
                result[bone_name] = \
                    result[bone_name] + \
                    TransformAnalysisHelper.calculate_transforms_discrepancy(    
                        self.trees[tree_index].get_node(key=bone_name).node.bone_transform,
                        self.trees[tree_index + 1].get_node(key=bone_name).node.bone_transform
                    )

        for factor in result.values():
            if FloatComparisonHelper.is_equal(factor, 0.0):
                raise ValueError('Monotonny detected in animation frames!')
