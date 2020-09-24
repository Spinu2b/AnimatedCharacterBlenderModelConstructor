

from acbmc.model.model.animated_character_description import AnimatedCharacterDescription


class AnimatedCharacterWithOneGlobalRootedArmatureConstructor:
    def construct_using(
        armature_bind_pose_model: ArmatureBindPoseModel,
        animated_character_description: AnimatedCharacterDescription, 
        allow_actual_zero_linear_interpolation_on_the_timeline: bool,
        allow_objects_having_actual_zero_scale: bool):
        raise NotImplementedError
