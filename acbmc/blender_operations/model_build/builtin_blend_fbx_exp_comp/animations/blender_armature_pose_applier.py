from bpy.types import Object
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.animations.blender_armature_bone_pose_setter_facade import BlenderArmatureBonePoseSetterFacade
from acbmc.blender_operations.blender_objects_manipulator import BlenderObjectsManipulator
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class BlenderArmaturePoseApplier:
    @classmethod
    def setup_pose_keyframe_in_animation_clip(
        cls,
        pose_armature_hierarchy: TreeHierarchy,
        blender_armature_obj: Object
    ):
        blender_objects_manipulator = BlenderObjectsManipulator()
        for animation_frame_bone_transform_node_iter in pose_armature_hierarchy.iterate_nodes():
            # setup only keyframed bones actually in particular frame number,
            # don't care 'bout the rest, as it should be
            if animation_frame_bone_transform_node_iter.node.is_keyframe:
                BlenderArmatureBonePoseSetterFacade.transform_bone_in_animation_frame(
                    blender_armature_obj,
                    animation_frame_bone_transform_node_iter.node
                )

                # in pose mode select only the bone currently being transformed and lock its rotation, scale and position (LocRotScale)

                blender_objects_manipulator.deselect_all_pose_objects()
                BlenderArmatureBonePoseSetterFacade.select_pose_bone(
                    animation_frame_bone_transform_node_iter.node.bone_name, blender_armature_obj)
                
                # raise NotImplementedError
                BlenderArmatureBonePoseSetterFacade.lock_rotation_scale_position()
                blender_objects_manipulator.deselect_all_pose_objects()
        # blender_objects_manipulator.deselect_all_pose_objects()
        # BlenderArmatureBonePoseSetterFacade.select_all_pose_bones()
