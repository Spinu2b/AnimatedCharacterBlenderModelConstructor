from acbmc.blender_operations.blender_objects_manipulator import BlenderObjectsManipulator
from typing import Dict, List
from bpy.types import Object
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.animations.blender_armature_pose_applier import BlenderArmaturePoseApplier
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode


class TreeHierarchyBonesPoseLocalTransformsConstructionHelper:
    @classmethod
    def construct_bones_keyframes_transforms_tree_hierarchy_for(
        cls,
        bones_keyframes: Dict[str, TransformNode],
        armature_hierarchy: TreeHierarchy
    ) -> TreeHierarchy:
        result_tree_hierarchy = TreeHierarchy()
        home_transform = TransformNode()
        for hierarchy_iter in armature_hierarchy.iterate_nodes():
            bone_name = hierarchy_iter.key  # type: str
            result_tree_hierarchy.add_node(
                parent_key=hierarchy_iter.parent_key,
                node_key=bone_name,
                node=BoneTransformNode.from_transform_node(
                    bone_name=bone_name,
                    transform_node=bones_keyframes[bone_name],
                    is_keyframe=True) if bone_name in bones_keyframes else
                    BoneTransformNode.from_transform_node(
                        bone_name=bone_name,
                        transform_node=home_transform,
                        is_keyframe=False))

        return result_tree_hierarchy


class BlenderArmatureAnimator:
    def __init__(self, blender_armature_obj: Object, armature_hierarchy: TreeHierarchy):
        self.blender_armature_obj = blender_armature_obj
        self.armature_hierarchy = armature_hierarchy
        self.bones_keyframes = dict()  # type: Dict[int, Dict[str, TransformNode]]

    def _add_keyframe_if_does_not_exist(self, keyframe_number: int):
        if keyframe_number not in self.bones_keyframes:
            self.bones_keyframes[keyframe_number] = dict()

    @classmethod
    def for_armature(cls, blender_armature_obj: Object, armature_hierarchy: TreeHierarchy) -> 'BlenderArmatureAnimator':
        return BlenderArmatureAnimator(blender_armature_obj, armature_hierarchy)

    def animate_bone(self, name: str, local_transform: TransformNode, keyframe_number: int) -> 'BlenderArmatureAnimator':
        self._add_keyframe_if_does_not_exist(keyframe_number)
        self.bones_keyframes[keyframe_number][name] = local_transform.copy()
        return self

    def commit(self) -> List[TreeHierarchy]:
        result_keyframes_local_bone_transforms_tree_hierarchies = []  # type: List[TreeHierarchy]
        blender_editor_manipulator = BlenderEditorManipulator()
        blender_objects_manipulator = BlenderObjectsManipulator()
        blender_editor_manipulator.enter_pose_mode_for_object_as_active_from_object_mode(self.blender_armature_obj)
        for keyframe_number in self.bones_keyframes:
            current_pose_hierarchy = \
                TreeHierarchyBonesPoseLocalTransformsConstructionHelper.construct_bones_keyframes_transforms_tree_hierarchy_for(
                    self.bones_keyframes[keyframe_number],
                    self.armature_hierarchy
                )

            blender_editor_manipulator.enter_frame_number(frame_number=keyframe_number)

            BlenderArmaturePoseApplier.setup_pose_keyframe_in_animation_clip(
                current_pose_hierarchy,
                self.blender_armature_obj
            )

            result_keyframes_local_bone_transforms_tree_hierarchies.append(current_pose_hierarchy)

        blender_editor_manipulator.enter_object_mode()
        return result_keyframes_local_bone_transforms_tree_hierarchies
