from typing import Dict, List
from bpy.types import PoseBone
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help \
         import UnifiedArmatureWithDeformSetsBonesNamingHelper
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
        result = []  # type: List[PoseBone]

        pose_bone_channel_id = \
                UnifiedArmatureWithDeformSetsBonesNamingHelper \
                    .get_channel_id_from_channel_bone_name(pose_bone.name)

        for chan_hierarchy in channel_hierarchies.values():
            if pose_bone_channel_id in chan_hierarchy.channel_hierarchy.parenting:
                parent_channel_id = chan_hierarchy.channel_hierarchy.parenting[pose_bone_channel_id]

                if parent_channel_id not in list(map(
                    lambda x: UnifiedArmatureWithDeformSetsBonesNamingHelper \
                        .get_channel_id_from_channel_bone_name(x.name), result)):
                    result \
                        .append(
                            next(y for y in armature_pose_bones
                             if UnifiedArmatureWithDeformSetsBonesNamingHelper \
                                .get_channel_id_from_channel_bone_name(y.name) == parent_channel_id))
                    
        return result
