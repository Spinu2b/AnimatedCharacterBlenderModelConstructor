from typing import Any, Dict, List, Tuple
from bpy.types import Armature, Object, Pose, PoseBone
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.bones_parenting.child_of_const_set_help import ChildOfConstraintSettingHelper
from acbmc.model.animated_character.model.subobjects_channels_associations_desc \
    .subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.util.collections_utils import CollectionsUtils
from acbmc.blender_operations.blender_editor_manipulator import BlenderEditorManipulator
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.impls.blender_skin_obj_with_arm_fact import BlenderSkinnedObjectsWithArmatureFactory


class BlenderSkinnedObjectsWithArmatureAnimatedChannelBonesParentingFactory:
    def _set_appropriate_child_of_constraints_to_channel_and_subobjects_deform_set_bones(
        self,
        blender_armature_obj: Object,
        channel_hierarchies: Dict[str, ChannelHierarchy],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation]
    ):
        blender_editor_manipulator = BlenderEditorManipulator()
        blender_editor_manipulator.enter_pose_mode_for_object_as_active_from_object_mode(blender_armature_obj)

        pose_data = blender_armature_obj.pose  # type: Pose

        pose_bones_list = \
            CollectionsUtils \
                .iterate_collection_and_return_copied_list(pose_data.bones)  # type: List[PoseBone]
        for pose_bone_el in pose_bones_list:
            pose_bone = pose_bone_el  # type: PoseBone
            ChildOfConstraintSettingHelper \
                .set_appropriate_child_of_constraint_to_bone(
                    pose_bone,
                    pose_bones_list,
                    channel_hierarchies,
                    subobjects_channels_associations,
                    blender_armature_obj
                )       
        
        blender_editor_manipulator.enter_object_mode()

    def build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
        self,
        base_armature_factory: BlenderSkinnedObjectsWithArmatureFactory,
        subobjects: Dict[int, Subobject],
        subobjects_mesh_objects: Dict[int, Object],
        channel_hierarchies: Dict[str, ChannelHierarchy],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation],
        armature_name: str,
        armature_constructing_data: Any) -> Tuple[Armature, Object]:

        _, blender_armature_obj = \
            base_armature_factory \
                .build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
                    subobjects,
                    subobjects_mesh_objects,
                    armature_name, 
                    armature_constructing_data
                )

        self._set_appropriate_child_of_constraints_to_channel_and_subobjects_deform_set_bones(
            blender_armature_obj,
            channel_hierarchies,
            subobjects_channels_associations,
        )
