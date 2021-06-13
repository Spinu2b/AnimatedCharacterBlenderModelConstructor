from typing import Any, Dict, List, Tuple
import bpy
from bpy.types import Armature, ChildOfConstraint, Object, Pose, PoseBone
from acbmc.util.collections_utils import CollectionsUtils
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_with_deform_sets_bones_nam_help import UnifiedArmatureWithDeformSetsBonesNamingHelper
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.bone_nodes.edit_mode_bone_nodes_factory import EditModeBoneNodesFactory
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_bind_pos_arm_model_with_chan_fact import BlenderBindPoseArmatureModelWithChannelsFactory
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.building.blender_arm_model_fact import BlenderArmatureModelFactory
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.impls.blender_skin_obj_with_arm_fact import BlenderSkinnedObjectsWithArmatureFactory


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
        blender_armature_obj: Object
    ):
        respective_bones_to_parent_to = \
                list(
                    filter(
                        lambda x: x.name != pose_bone.name and
                        UnifiedArmatureWithDeformSetsBonesNamingHelper
                            .is_channel_bone_name(x.name), armature_pose_bones))

        for parent_bone in respective_bones_to_parent_to:
            cls._set_child_of_constraint_between_bones(
                pose_bone,
                parent_bone,
                blender_armature_obj
            )


class BlenderSkinnedObjectsWithArmatureAnimatedChannelBonesParentingFactory(
    BlenderSkinnedObjectsWithArmatureFactory):
    def __init__(self):
        super().__init__(BlenderBindPoseArmatureModelWithChannelsFactory(EditModeBoneNodesFactory()))

    def _set_appropriate_child_of_constraints_to_channel_and_subobjects_deform_set_bones(
        self,
        blender_armature_obj: Object,
        armature_model: TreeHierarchy
    ):
        blender_editor_manipulator = BlenderEditorManipulator()
        blender_editor_manipulator.enter_pose_mode_for_object_as_active_from_object_mode(blender_armature_obj)

        pose_data = blender_armature_obj.pose  # type: Pose

        pose_bones_list = \
            CollectionsUtils \
                .iterate_collection_and_return_copied_list(pose_data.bones)  # type: List[PoseBone]
        for pose_bone_el in pose_bones_list:
            pose_bone = pose_bone_el  # type: PoseBone
            ChildOfConstraintSettingHelper.set_appropriate_child_of_constraint_to_bone(
                pose_bone, pose_bones_list, blender_armature_obj)       
        
        blender_editor_manipulator.enter_object_mode()

    def build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
        self,
        subobjects: Dict[int, Subobject],
        subobjects_mesh_objects: Dict[int, Object],
        armature_bind_pose_model: TreeHierarchy,
        channel_hierarchies: Dict[str, ChannelHierarchy],
        armature_name: str,
        armature_constructing_data: Any) -> Tuple[Armature, Object]:

        blender_armature_data_block, blender_armature_obj = \
            super().build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
                subobjects,
                subobjects_mesh_objects,
                armature_bind_pose_model,
                channel_hierarchies,
                armature_name, 
                armature_constructing_data
            )

        blender_edit_mode_armature_model = \
            self.blender_edit_mode_armature_model_factory \
                .get_blender_armature_model(armature_constructing_data)  # type: TreeHierarchy

        self._set_appropriate_child_of_constraints_to_channel_and_subobjects_deform_set_bones(
            blender_armature_obj,
            blender_edit_mode_armature_model
        )
