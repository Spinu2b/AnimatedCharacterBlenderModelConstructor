from typing import Dict, List, Tuple
from bpy.types import Object
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature \
        .building.blender_edit_mode_arm_model_fact import EditModeBoneNodeDataFactory
from acbmc.model.blender.model.armature.edit_mode_bone_node import EditModeBoneNode
from acbmc.util.tree_iteration_helper import TreeIterationHelper
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.constructing \
    .armature.blender_armature_constructor import BlenderArmatureConstructor
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode


class BlenderArmatureBuilderBlenderEditModeArmatureModelFactory:
    @classmethod
    def get_blender_edit_mode_armature_model(
        cls, bones_edit_mode_transforms: List[Tuple[str, TransformNode]], bones_parentings: Dict[str, str]) \
         -> Tuple[TreeHierarchy, TreeHierarchy]:

        blender_edit_mode_armature_model = TreeHierarchy()
        world_transform_bones_tree_hierarchy = TreeHierarchy()

        for bone_transform_info in TreeIterationHelper.iterate_sequence_in_order_of_tree_building(
            collection=bones_edit_mode_transforms,
            parent_key_getter=lambda x: bones_parentings[x[0]] if x[0] in bones_parentings else None,
            node_key_getter=lambda x: x[0]):

            edit_mode_bone_node = EditModeBoneNode()
            edit_mode_bone_node.bone_name = bone_transform_info[0]

            head_position, tail_position = EditModeBoneNodeDataFactory.get_head_and_tail_position_from(bone_transform_info[1])
            edit_mode_bone_node.head_position = head_position
            edit_mode_bone_node.tail_position = tail_position

            blender_edit_mode_armature_model.add_node(
                parent_key=bones_parentings[bone_transform_info[0]] if bone_transform_info[0] in bones_parentings else None,
                node_key=bone_transform_info[0],
                node=edit_mode_bone_node
            )

            world_transform_bones_tree_hierarchy.add_node(
                parent_key=bones_parentings[bone_transform_info[0]] if bone_transform_info[0] in bones_parentings else None,
                node_key=bone_transform_info[0],
                node=BoneTransformNode.from_transform_node(bone_name=bone_transform_info[0], transform_node=bone_transform_info[1])
            )

        return blender_edit_mode_armature_model, world_transform_bones_tree_hierarchy

class BlenderArmatureBuilder:
    def __init__(self):
        self.armature_name = None  # type: str
        self.bones_edit_mode_transforms = []  # type: List[Tuple[str, TransformNode]]
        self.bones_parentings = dict()  # type: Dict[str, str]

    def with_armature_name(self, armature_name: str) -> 'BlenderArmatureBuilder':
        self.armature_name = armature_name
        return self

    def with_bone(self, name: str, transform: TransformNode) -> 'BlenderArmatureBuilder':
        self.bones_edit_mode_transforms.append((name, transform.copy()))
        return self

    def parent_bones(self, child: str, parent: str) -> 'BlenderArmatureBuilder':
        self.bones_parentings[child] = parent
        return self

    def build(self) -> Tuple[Object, TreeHierarchy]:
        blender_edit_mode_armature_model, world_transform_bones_tree_hierarchy = \
            BlenderArmatureBuilderBlenderEditModeArmatureModelFactory.get_blender_edit_mode_armature_model(
                bones_edit_mode_transforms=self.bones_edit_mode_transforms,
                bones_parentings=self.bones_parentings
            )

        _, blender_armature_obj = BlenderArmatureConstructor().build_armature(
            blender_edit_mode_armature_model=blender_edit_mode_armature_model,
            name=self.armature_name
        )

        blender_editor_manipulator = BlenderEditorManipulator()
        blender_editor_manipulator.enter_object_mode()
        return blender_armature_obj, world_transform_bones_tree_hierarchy
