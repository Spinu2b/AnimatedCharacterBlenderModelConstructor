import copy
import statistics
from typing import Dict, List
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.helpers.monotony_analyzer import MonotonyAnalyzer
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
        rotation_discrepancy = (transform_a.rotation - transform_b.rotation).abs()
        scale_discrepancy = (transform_a.scale - transform_b.scale).magnitude()

        return position_discrepancy + rotation_discrepancy + scale_discrepancy


class AnimationFramesTreesMonotonyAnalyzer(MonotonyAnalyzer):
    def consider_tree(self, tree_hierarchy: TreeHierarchy):
        self.consider(copy.deepcopy(tree_hierarchy))

    def raise_exception_if_monotonous(self):
        result = dict()  # type: Dict[str, float]

        for tree_index in range(len(self.elements) - 1):
            for bone_name in \
                TreeHierarchiesAnalysisConsolidationHelper.get_corresponding_bones_name_keyframes_in_trees(
                    self.elements[tree_index], self.elements[tree_index + 1]):
                if bone_name not in result:
                    result[bone_name] = []
                
                result[bone_name].append(
                    TransformAnalysisHelper.calculate_transforms_discrepancy(    
                        self.elements[tree_index].get_node(key=bone_name).node.bone_transform,
                        self.elements[tree_index + 1].get_node(key=bone_name).node.bone_transform
                    ))

        result_values = dict()  # type: Dict[int, float]
        for bone_name in result:
            result_values[bone_name] = float(statistics.mean(result[bone_name]))

        for factor in result_values.values():
            if not FloatComparisonHelper.is_close_to(factor, 0.0):
                return
                             
        raise ValueError('Monotony detected in animation frames!')
