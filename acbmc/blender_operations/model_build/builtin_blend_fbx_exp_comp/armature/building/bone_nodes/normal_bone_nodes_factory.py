from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.bone_nodes_factory import BoneNodesFactory


class NormalBoneNodesFactory(BoneNodesFactory):
    def get_bone_node(
        self, bone_bind_pose: TransformNode, bone_name: str) -> BoneTransformNode:
        return BoneTransformNode.from_transform_node(bone_name=bone_name, transform_node=bone_bind_pose)

    def get_home_transformed_bone_node(self, bone_name: str) -> BoneTransformNode:
        result = BoneTransformNode()
        result.bone_name = bone_name
        return result
