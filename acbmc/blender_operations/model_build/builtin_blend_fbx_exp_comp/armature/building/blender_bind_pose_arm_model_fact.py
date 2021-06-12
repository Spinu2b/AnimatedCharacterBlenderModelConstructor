from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.normal_bone_nodes_factory import NormalBoneNodesFactory
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_arm_model_fact import BlenderArmatureModelFactory


class BlenderBindPoseArmatureModelFactory(BlenderArmatureModelFactory):
    def __init__(self):
        super().__init__(NormalBoneNodesFactory())
