from typing import Any, Dict
from abc import ABC, abstractmethod
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.node_trav_impls \
    .subobj_bon_on_arm_mod_build_impl import SubobjectsBonesOnlyArmatureModelBuilderImplementation
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature \
    .uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.transform_node import TransformNode

class BlenderArmatureModelFactory(ABC):
    @abstractmethod
    def get_appropriate_subobject_actual_bone_node(self, bone_bind_pose: TransformNode, bone_name: str) -> Any:
        raise ValueError

    @abstractmethod
    def get_appropriate_subobject_parent_bone_node(self, bone_name: str) -> Any:
        raise ValueError

    def __init__(self):
        self.armature_model_builder_implementation = SubobjectsBonesOnlyArmatureModelBuilderImplementation(self)

    def get_blender_armature_model(
        self, data: any) -> TreeHierarchy:
        return self.armature_model_builder_implementation.get_blender_armature_model(data)
