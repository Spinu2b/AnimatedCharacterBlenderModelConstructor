from typing import Callable, Dict
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class AnimationClips:
    def __init__(self):
        self.animation_clips = dict()  # type: Dict[int, AnimationClip]

    def reform_space_model(
        self,
        position3d_transformation: Callable[[Vector3d], None],
        rotation_transformation: Callable[[Quaternion], None]
    ):
        for anim_clip in self.animation_clips.values():
            anim_clip.reform_space_model(
                position3d_transformation=position3d_transformation,
                rotation_transformation=rotation_transformation
            )
