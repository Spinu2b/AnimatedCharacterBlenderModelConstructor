from typing import Dict, List
from bpy.types import PoseBone
from acbmc.model.animated_character.model \
    .subobjects_channels_associations_desc \
        .subobjects_channels_association import SubobjectsChannelsAssociation


class DeformSetBoneAnimatedParentingDeterminerHelper:
    @classmethod
    def get_possible_pose_bone_parents(
        cls,
        pose_bone: PoseBone,
        armature_pose_bones: List[PoseBone],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation]
    ) -> List[PoseBone]:
        raise NotImplementedError
