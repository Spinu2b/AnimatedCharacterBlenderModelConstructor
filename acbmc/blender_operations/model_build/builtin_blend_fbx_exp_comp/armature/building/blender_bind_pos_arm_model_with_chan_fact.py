from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.node_trav_impls \
    .with_chan_bon_arm_mod_build_impl import WithChannelsBonesArmatureModelBuilderImplementation
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_bind_pose_arm_model_fact import BlenderBindPoseArmatureModelFactory


class BlenderBindPoseArmatureModelWithChannelsFactory(BlenderBindPoseArmatureModelFactory):
    def __init__(self):
        self.armature_model_builder_implementation = WithChannelsBonesArmatureModelBuilderImplementation(self)
