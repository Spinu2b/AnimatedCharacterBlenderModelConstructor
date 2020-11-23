from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper


class UnifiedArmatureTreeHierarchyHelper:
    @staticmethod
    def make_armature_tree_hierarchy_having_one_root(armature_tree_hierarchy: TreeHierarchy):
        root_node_key = UnifiedArmatureWithDeformSetsBonesNamingHelper.get_bone_name_for_root_channel()  # type: str
        root_channel_transform_node = BoneTransformNode()
        root_channel_transform_node.bone_name = root_node_key
        armature_tree_hierarchy.parent_current_roots_to_new_root(
            node_key=root_node_key,
            node=root_channel_transform_node
        )        
