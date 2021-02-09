from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_arm_model_fact import BlenderArmatureModelFactory


class BlenderBindPoseArmatureModelFactory(BlenderArmatureModelFactory):
    def _get_appropriate_subobject_actual_bone_node(
        self, bone_bind_pose: TransformNode, bone_name: str) -> BoneTransformNode:
        return BoneTransformNode.from_transform_node(bone_name=bone_name, transform_node=bone_bind_pose)

    def _get_appropriate_subobject_parent_bone_node(self, bone_name: str) -> BoneTransformNode:
        result = BoneTransformNode()
        result.bone_name = bone_name
        return result
