
from typing import Dict, List
from bpy.types import PoseBone
from acbmc.model.animated_character.model \
    .channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChannelBoneAnimatedParentingDeterminerHelper:
    @classmethod
    def get_possible_pose_bone_parents(
        cls, 
        pose_bone: PoseBone,
        armature_pose_bones: List[PoseBone],
        channel_hierarchies: Dict[str, ChannelHierarchy]
    ) -> List[PoseBone]:
        raise NotImplementedError
