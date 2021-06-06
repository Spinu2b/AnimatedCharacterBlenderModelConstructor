import bpy
import mathutils
from bpy.types import Object, Pose, PoseBone
from acbmc.model.blender.model.armature.bone_transform_node import BoneTransformNode


class BlenderArmatureBonePoseSetterFacade:
    @classmethod
    def transform_bone_in_animation_frame(
        cls,
        blender_armature_obj: Object,
        bone_transform_node: BoneTransformNode
    ):
        pose = blender_armature_obj.pose  # type: Pose
        complementary_pose_bone = pose.bones.get(bone_transform_node.bone_name)  # type: PoseBone
        complementary_pose_bone.rotation_mode = 'QUATERNION'

        loc = mathutils.Matrix.Translation(mathutils.Vector((
            bone_transform_node.bone_transform.position.x,
            bone_transform_node.bone_transform.position.y,
            bone_transform_node.bone_transform.position.z,
        )))

        rot = mathutils.Quaternion(mathutils.Vector((
            bone_transform_node.bone_transform.rotation.w,
            bone_transform_node.bone_transform.rotation.x,
            bone_transform_node.bone_transform.rotation.y,
            bone_transform_node.bone_transform.rotation.z
        ))).to_matrix().to_4x4()

        scale = mathutils.Matrix()
        # scale.zero()

        scale[0][0] = bone_transform_node.bone_transform.scale.x
        scale[1][1] = bone_transform_node.bone_transform.scale.y
        scale[2][2] = bone_transform_node.bone_transform.scale.z

        world_mat = loc @ rot @ scale

        # complementary_pose_bone.matrix = world_mat

        complementary_pose_bone.matrix = blender_armature_obj.convert_space(
            pose_bone=complementary_pose_bone,
            matrix=world_mat,
            from_space='LOCAL',
            to_space='LOCAL'
        )

    @classmethod
    def lock_rotation_scale_position(cls):
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

    @classmethod
    def select_pose_bone(cls, bone_name: str, blender_armature_obj: Object):
        pose = blender_armature_obj.pose  # type: Pose
        complementary_pose_bone = pose.bones.get(bone_name)  # type: PoseBone

        complementary_pose_bone.bone.select = True
        complementary_pose_bone.bone.select_tail = True
        complementary_pose_bone.bone.select_head = True
