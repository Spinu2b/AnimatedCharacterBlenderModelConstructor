from typing import Dict, List
from bpy.types import PoseBone
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.bones_parenting.deform_set.def_set_act_bon_ani_par_det_hel \
         import DeformSetActualBoneAnimatedParentingDeterminerHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.bones_parenting.deform_set.subobj_gov_bon_anim_par_det_help \
         import SubobjectGoverningBoneAnimatedParentingDeterminerHelper
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help \
        import UnifiedArmatureWithDeformSetsBonesNamingHelper
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
        if UnifiedArmatureWithDeformSetsBonesNamingHelper.is_deform_set_subobject_governing_bone(pose_bone.name):
            result = SubobjectGoverningBoneAnimatedParentingDeterminerHelper.get_possible_pose_bone_parents(
                pose_bone,
                armature_pose_bones,
                subobjects_channels_associations
            )
        elif UnifiedArmatureWithDeformSetsBonesNamingHelper.is_deform_set_actual_bone(pose_bone.name):
            result =  DeformSetActualBoneAnimatedParentingDeterminerHelper.get_possible_pose_bone_parents(
                pose_bone,
                armature_pose_bones,
                subobjects_channels_associations
            )
        else:
            raise ValueError("Unrecognized bone type {}".format(pose_bone.name))

        return result
