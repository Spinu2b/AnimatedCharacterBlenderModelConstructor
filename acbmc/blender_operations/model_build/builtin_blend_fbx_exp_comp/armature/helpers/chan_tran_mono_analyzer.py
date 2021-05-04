import copy
import statistics
from typing import Dict, List
from acbmc.util.float_comparison_helper import FloatComparisonHelper
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.helpers.anim_fram_tree_mono_analyzer import TransformAnalysisHelper
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.helpers.monotony_analyzer import MonotonyAnalyzer
from acbmc.util.model.transform_node import TransformNode


class ChannelTransformsConsolidationAnalysisHelper:
    @classmethod
    def get_corresponding_channel_id(
        cls,
        channel_transforms_a: Dict[int, TransformNode],
        channel_transforms_b: Dict[int, TransformNode]) -> List[str]:
        result = []  # type: List[int]
    
        for channel_id in channel_transforms_a:
            if channel_id in channel_transforms_b:
                result.append(channel_id)

        return result


class ChannelTransformsMonotonyAnalyzer(MonotonyAnalyzer):
    def consider_channel_transforms(self, channel_transforms: Dict[int, TransformNode]):
        self.consider(copy.deepcopy(channel_transforms))

    def raise_exception_if_monotonous(self):
        result = dict()  # type: Dict[int, float]

        for channel_transforms_index in range(len(self.elements) - 1):
            for channel_id in ChannelTransformsConsolidationAnalysisHelper.get_corresponding_channel_id(
                self.elements[channel_transforms_index], self.elements[channel_transforms_index + 1]
            ):

                if channel_id not in result:
                    result[channel_id] = []

                result[channel_id].append(
                        TransformAnalysisHelper.calculate_transforms_discrepancy(    
                            self.elements[channel_transforms_index][channel_id],
                            self.elements[channel_transforms_index + 1][channel_id]
                        ))

        result_values = dict()  # type: Dict[int, float]
        for channel_id in result:
            result_values[channel_id] = float(statistics.mean(result[channel_id]))
        
        for factor in result_values.values():
            if not FloatComparisonHelper.is_close_to(factor, 0.0):
                return
        raise ValueError('Monotony detected in channel transforms!')        
