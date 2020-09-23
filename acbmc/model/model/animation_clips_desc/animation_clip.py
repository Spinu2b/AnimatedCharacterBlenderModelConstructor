
from acbmc.model.model.animation_clips_desc.subobject_used_morph_association_info import SubobjectUsedMorphAssociationInfo
from typing import Dict, List
from acbmc.model.model.animation_clips_desc.channel_transform import ChannelTransform
from acbmc.model.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo


class AnimationClip:
    def __init__(self):
        self.id = -1  # type: int
        self.channel_keyframes = dict()  # type: Dict[int, Dict[int, ChannelTransform]]
        self.channels_for_subobjects_associations_data = dict()  # type: Dict[str, List[AnimationFramesPeriodInfo]]
        self.animation_hierarchies = dict()  # type: Dict[str, List[AnimationFramesPeriodInfo]]
        self.morphs = []  # type: List[SubobjectUsedMorphAssociationInfo]
