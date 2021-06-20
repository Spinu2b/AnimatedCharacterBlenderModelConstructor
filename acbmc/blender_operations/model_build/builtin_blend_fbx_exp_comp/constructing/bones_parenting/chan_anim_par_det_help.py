from typing import Dict, List
from bpy.types import PoseBone
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.bones_parenting.def_set_bon_anim_par_det_help \
        import DeformSetBoneAnimatedParentingDeterminerHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.bones_parenting.chan_bon_anim_par_det_help \
         import ChannelBoneAnimatedParentingDeterminerHelper
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature \
        .uni_arm_with_deform_sets_bones_nam_help \
            import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model \
    .subobjects_channels_associations_desc \
        .subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model \
    .channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChannelsAnimatedParentingDeterminerHelper:
    def get_possible_pose_bone_parents(
        pose_bone: PoseBone,
        armature_pose_bones: List[PoseBone],
        channel_hierarchies: Dict[str, ChannelHierarchy],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation]) -> List[PoseBone]:
        result = []  # type: List[PoseBone]

        if UnifiedArmatureWithDeformSetsBonesNamingHelper.is_channel_bone_name(pose_bone.name):
            result = ChannelBoneAnimatedParentingDeterminerHelper.get_possible_pose_bone_parents(
                pose_bone,
                armature_pose_bones,
                channel_hierarchies
            )
        elif UnifiedArmatureWithDeformSetsBonesNamingHelper.is_deform_set_bone(pose_bone.name):
            result = DeformSetBoneAnimatedParentingDeterminerHelper.get_possible_pose_bone_parents(
                pose_bone,
                armature_pose_bones,
                subobjects_channels_associations
            )
        else:
            raise ValueError("Unrecognized bone type {}".format(pose_bone.name))

        return result
