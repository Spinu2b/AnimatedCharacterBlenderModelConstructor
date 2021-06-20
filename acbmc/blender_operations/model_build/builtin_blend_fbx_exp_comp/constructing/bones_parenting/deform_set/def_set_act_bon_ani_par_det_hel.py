from typing import Dict, List
from bpy.types import PoseBone
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help \
        import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.model.animated_character.model \
    .subobjects_channels_associations_desc \
        .subobjects_channels_association import SubobjectsChannelsAssociation


class DeformSetActualBoneAnimatedParentingDeterminerHelper:
    @classmethod
    def _appropriate_channel_bone_predicate(
        cls,
        pose_bone: PoseBone,
        considered_deform_set_bone: PoseBone,
        channels_for_subobjects_bones_parenting: Dict[int, Dict[int, List[int]]]) -> bool:
        if (not UnifiedArmatureWithDeformSetsBonesNamingHelper.is_channel_bone_name(pose_bone.name)):
            return False

        channel_id = \
            UnifiedArmatureWithDeformSetsBonesNamingHelper \
                .get_channel_id_from_channel_bone_name(pose_bone.name)

        subobject_index, subobject_bone_index = \
            UnifiedArmatureWithDeformSetsBonesNamingHelper \
                .get_subobject_index_and_bone_index_for_subobject_deform_set_bone(
                    considered_deform_set_bone.name
                )

        return channel_id in channels_for_subobjects_bones_parenting and \
             subobject_index in channels_for_subobjects_bones_parenting[channel_id] and \
            subobject_bone_index in channels_for_subobjects_bones_parenting[channel_id][subobject_index]

    @classmethod
    def get_possible_pose_bone_parents(
        cls,
        pose_bone: PoseBone,
        armature_pose_bones: List[PoseBone],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation]) -> List[PoseBone]:
        
        result = []  # type: List[PoseBone]

        for subobj_chan_assoc in subobjects_channels_associations.values():
            subobj_chan_assoc_desc = subobj_chan_assoc.subobjects_channels_associations_description
            channels_for_subobjects_bones_parenting = subobj_chan_assoc_desc.channels_for_subobjects_bones_parenting

            governing_channel_bone_candidate = \
                next((bone for bone in armature_pose_bones if 
                        cls._appropriate_channel_bone_predicate(
                            bone,
                            pose_bone,
                            channels_for_subobjects_bones_parenting)),
                        None)  # type: PoseBone
            if governing_channel_bone_candidate is not None:
                result.append(governing_channel_bone_candidate)

        return result
