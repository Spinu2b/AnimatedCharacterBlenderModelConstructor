
from typing import Dict, List
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.model.animation_clips_desc.subobject_used_morph_association_info import SubobjectUsedMorphAssociationInfo
from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo


class AnimationClip:
    def __init__(self):
        self.id = -1  # type: int
        self.channel_keyframes = dict()  # type: Dict[int, Dict[int, TransformNode]]
        self.channels_for_subobjects_associations_data = dict()  # type: Dict[str, List[AnimationFramesPeriodInfo]]
        self.animation_hierarchies = dict()  # type: Dict[str, List[AnimationFramesPeriodInfo]]
        self.morphs = []  # type: List[SubobjectUsedMorphAssociationInfo]

    def get_frames_count(self) -> int:
        return max(x.frame_end for sublist in self.animation_hierarchies.values() for x in sublist)
