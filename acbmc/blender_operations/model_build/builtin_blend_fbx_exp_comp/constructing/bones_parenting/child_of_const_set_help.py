from typing import Dict, List
import bpy
from bpy.types import ChildOfConstraint, Object, PoseBone
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.bones_parenting \
        .chan_anim_par_det_help import ChannelsAnimatedParentingDeterminerHelper
from acbmc.model.animated_character.model.subobjects_channels_associations_desc \
    .subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model \
    .channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy


class ChildOfConstraintSettingHelper:
    @classmethod
    def _set_child_of_constraint_between_bones(
        cls,
        child_pose_bone: PoseBone,
        parent_pose_bone: PoseBone,
        blender_armature_obj: Object
    ):
        child_of_constraint = child_pose_bone.constraints.new(type="CHILD_OF")  # type: ChildOfConstraint
        context_py = bpy.context
        # bpy.ops.constraint.childof_set_inverse(constraint="Child Of", owner="BONE")
        child_of_constraint.target = blender_armature_obj
        child_of_constraint.subtarget = parent_pose_bone.name
        child_of_constraint.active = True
        child_of_constraint.influence = 0.0

    @classmethod
    def set_appropriate_child_of_constraint_to_bone(
        cls,
        pose_bone: PoseBone,
        armature_pose_bones: List[PoseBone],
        channel_hierarchies: Dict[str, ChannelHierarchy],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation],
        blender_armature_obj: Object
    ):
        respective_bones_to_parent_to = \
            ChannelsAnimatedParentingDeterminerHelper.get_possible_pose_bone_parents(
                pose_bone,
                armature_pose_bones,
                channel_hierarchies,
                subobjects_channels_associations
            )

        for parent_bone in respective_bones_to_parent_to:
            cls._set_child_of_constraint_between_bones(
                pose_bone,
                parent_bone,
                blender_armature_obj
            )