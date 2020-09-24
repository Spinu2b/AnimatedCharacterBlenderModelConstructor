
from typing import Dict
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class AnimationClips:
    def __init__(self):
        self.animation_clips = dict()  # type: Dict[int, AnimationClip]
