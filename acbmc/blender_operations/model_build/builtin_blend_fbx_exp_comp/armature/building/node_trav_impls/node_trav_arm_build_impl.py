from abc import ABC, abstractmethod
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature.building.blender_arm_model_fact import BlenderArmatureModelFactory
from acbmc.util.model.tree_hierarchy import TreeHierarchy

class NodeTraversalArmatureBuildingImplementation(ABC):
    def __init__(self, blender_armature_model_factory: 'BlenderArmatureModelFactory'):
        self.blender_armature_model_factory = blender_armature_model_factory

    @abstractmethod
    def get_blender_armature_model(self, data: any) -> TreeHierarchy:
        raise ValueError
