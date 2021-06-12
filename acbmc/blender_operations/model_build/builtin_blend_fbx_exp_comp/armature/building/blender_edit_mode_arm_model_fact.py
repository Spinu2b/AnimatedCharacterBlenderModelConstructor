from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.edit_mode_bone_nodes_factory import EditModeBoneNodesFactory
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_arm_model_fact import BlenderArmatureModelFactory


class BlenderEditModeArmatureModelFactory(BlenderArmatureModelFactory):
    def __init__(self):
        super().__init__(EditModeBoneNodesFactory())
