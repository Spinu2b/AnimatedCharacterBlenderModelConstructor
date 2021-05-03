from acbmc.util.model.matrix4x4 import Matrix4x4
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_tree_hierarch_to_only_def_set_bones_flat import BoneMatrixHelper
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.scene_setups.util.armature.blender_armature_animator import BlenderArmatureAnimator
from acbmc.scene_setups.util.armature.blender_armature_builder import BlenderArmatureBuilder
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.blender_scene_manipulator import BlenderSceneManipulator


class SimpleCaseMatricesCalculationVerificationLogic:
    # it works ok here
    def execute(self):
        BlenderSceneManipulator().clear_scene()

        home_transform = TransformNode()

        first_keyframe = 0
        second_keyframe = 5

        test_armature_obj, test_armature_tree_hierarchy = \
            BlenderArmatureBuilder() \
            .with_armature_name(armature_name="TEST_ARMATURE") \
            .with_bone(name="BONE_A", transform=home_transform) \
            .with_bone(name="BONE_B", transform=home_transform) \
            .build()        

        animated_armature_tree_hierarchies = BlenderArmatureAnimator \
            .for_armature(test_armature_obj, test_armature_tree_hierarchy) \
            .animate_bone(name="BONE_A",
                          local_transform=
                            TransformNode.construct_with(
                                position=Vector3d(0.3, 0.5, 0.7),
                                rotation=Quaternion(),
                                scale=Vector3d(0.2, 0.4, 0.6)
                            ),
                          keyframe_number=first_keyframe) \
            .animate_bone(name="BONE_A",
                          local_transform=
                            TransformNode.construct_with(
                                position=Vector3d(0.9, 0.1, 0.3),
                                rotation=Quaternion(),
                                scale=Vector3d(0.6, 1.6, 1.3)
                            ),
                          keyframe_number=second_keyframe) \
            .commit()

        calculated_bone_animation_world_matrix_a = BoneMatrixHelper.get_world_matrix_for_bone(
                    "BONE_A", animated_armature_tree_hierarchies[0])  # type: Matrix4x4
        calculated_bone_animation_world_matrix_b = BoneMatrixHelper.get_world_matrix_for_bone(
                    "BONE_A", animated_armature_tree_hierarchies[1])  # type: Matrix4x4

        
        BlenderArmatureAnimator \
            .for_armature(test_armature_obj, test_armature_tree_hierarchy) \
            .animate_bone(
                 name="BONE_B",
                 local_transform=TransformNode.from_matrix4x4(calculated_bone_animation_world_matrix_a),
                 keyframe_number=first_keyframe) \
            .animate_bone(
                name="BONE_B",
                local_transform=TransformNode.from_matrix4x4(calculated_bone_animation_world_matrix_b),
                keyframe_number=second_keyframe) \
            .commit()
        