from typing import List, Tuple
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class PoseHierarchySubobjectsUsageHelper:
    @classmethod
    def zero_out_not_used_subobjects_bones_transformations_adding_them_to_pose_hierarchy(
        cls, pose_hierarchy: TreeHierarchy, all_actual_armature_bones_names: List[str]
    ):
        for armature_bone_name in all_actual_armature_bones_names:
            if not pose_hierarchy.contains_node_key(armature_bone_name):
                effectively_zeroed_scale_out_transform_node = TransformNode()
                effectively_zeroed_scale_out_transform_node.scale = Vector3d(0.0, 0.0, 0.0)

                pose_hierarchy.add_node(
                    parent_key=UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_root_channel(),
                    node_key=armature_bone_name,
                    node=BoneTransformNode.from_transform_node(
                        bone_name=armature_bone_name, transform_node=effectively_zeroed_scale_out_transform_node, is_keyframe=True)
                )


class PoseHierarchiesForSubobjectsUsageConsolidationTransformer:
    @classmethod
    def analyze_and_transform_the_pose_hierarchies_list_considering_subobjects_usage_and_prepare_appropriately_keyframed_final_pose_armature_hierarchies(
        cls,
        pose_hierarchies_in_animation_clip_infos: List[Tuple[int, TreeHierarchy]],
        armature_bind_pose_hierarchy: TreeHierarchy
    ):
        # don't bother with performance, just do it, analytically

        all_actual_armature_bones_names = [x.node.bone_name for x in armature_bind_pose_hierarchy.iterate_nodes()]  # type: List[str]

        # for now just zero out not used bones transforms in poses - that way when subobjects appear during animation
        # they will be linearly scaled up during frames due to not keyframing that fact

        # we might deal with that with yet another step in processing later (adding dedicated keyframed frames for like zero/close-to-zero linear
        # interpolation for suddenly appearing/disappearing subobjects)
        for pose_hierarchy_info in pose_hierarchies_in_animation_clip_infos:
            PoseHierarchySubobjectsUsageHelper.zero_out_not_used_subobjects_bones_transformations_adding_them_to_pose_hierarchy(
                pose_hierarchy_info[1], all_actual_armature_bones_names
            )
        
        # raise NotImplementedError
