from acbmc.model.blender.model.armature.armature_bind_pose_model import ArmatureBindPoseModel
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription


class AnimatedCharacterWithOneGlobalRootedArmatureConstructor:
    def construct_using(
        self,
        armature_bind_pose_model: ArmatureBindPoseModel,
        animated_character_description: AnimatedCharacterDescription, 
        allow_actual_zero_linear_interpolation_on_the_timeline: bool,
        allow_objects_having_actual_zero_scale: bool,
        parent_every_bone_to_root_using_regular_constant_child_parent_constraint: bool):
        raise NotImplementedError
