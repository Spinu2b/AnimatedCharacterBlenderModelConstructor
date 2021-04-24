from typing import List
from acbmc.scene_setups.bone_world_matrices \
    .transforms.disp_chain_bones_trans_fact import DisplacedChainedBonesTransformsFactory
from acbmc.scene_setups.bone_world_matrices.transforms.chain_bon_trans_fact import ChainedBonesTransformsFactory
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.scene_setups.util.armature \
    .blender_arm_bone_curr_anim_dat_help import BlenderArmatureBoneCurrentAnimationDataHelper
from acbmc.scene_setups.util.armature.blender_armature_animator import BlenderArmatureAnimator
from acbmc.scene_setups.util.armature.blender_armature_builder import BlenderArmatureBuilder
from acbmc.util.model.transform_node import TransformNode
from acbmc.util.model.matrix4x4 import Matrix4x4
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_arm_tree_hierarch_to_only_def_set_bones_flat import BoneMatrixHelper


class BoneWorldMatricesCalculationVerificationLogic:
    def _synthetic_transformation_verification_example(self):
        home_transform = TransformNode()

        first_keyframe = 0
        second_keyframe = 10

        chained_armature_chained_bones_transforms = \
            ChainedBonesTransformsFactory.get_armature_chained_bones_transforms_for(
                bones_count=7
            )  # type: List[TransformNode]

        blender_flat_armature_obj, blender_flat_armature_tree_hierarchy = \
            BlenderArmatureBuilder() \
            .with_armature_name("SYNTHETIC_EXAMPLE_FLAT_ARMATURE") \
            .with_bone(name="E1_BONE_TOP", transform=home_transform) \
            .with_bone(name="E1_BONE_BOTTOM", transform=chained_armature_chained_bones_transforms[6]) \
            .parent_bones(child="E1_BONE_BOTTOM", parent="E1_BONE_TOP") \
            .build()

        blender_parented_armature_obj, blender_parented_armature_tree_hierarchy = \
             BlenderArmatureBuilder() \
            .with_armature_name("SYNTHETIC_EXAMPLE_PARENTED_ARMATURE") \
            .with_bone(name="E2_BONE_TOP", transform=home_transform) \
            .with_bone(name="E2_BONE_CHAIN_1", transform=chained_armature_chained_bones_transforms[1]) \
            .with_bone(name="E2_BONE_CHAIN_2", transform=chained_armature_chained_bones_transforms[2]) \
            .with_bone(name="E2_BONE_CHAIN_3", transform=chained_armature_chained_bones_transforms[3]) \
            .with_bone(name="E2_BONE_CHAIN_4", transform=chained_armature_chained_bones_transforms[4]) \
            .with_bone(name="E2_BONE_CHAIN_5", transform=chained_armature_chained_bones_transforms[5]) \
            .with_bone(name="E2_BONE_BOTTOM", transform=chained_armature_chained_bones_transforms[6]) \
            .parent_bones(child="E2_BONE_BOTTOM", parent="E2_BONE_CHAIN_5") \
            .parent_bones(child="E2_BONE_CHAIN_5", parent="E2_BONE_CHAIN_4") \
            .parent_bones(child="E2_BONE_CHAIN_4", parent="E2_BONE_CHAIN_3") \
            .parent_bones(child="E2_BONE_CHAIN_3", parent="E2_BONE_CHAIN_2") \
            .parent_bones(child="E2_BONE_CHAIN_2", parent="E2_BONE_CHAIN_1") \
            .parent_bones(child="E2_BONE_CHAIN_1", parent="E2_BONE_TOP") \
            .build()

        displaced_chained_bones_transforms_first_keyframe = DisplacedChainedBonesTransformsFactory.get_displaced_transforms_for(
            bones_count=7,
            seed=1
        )

        displaced_chained_bones_transforms_second_keyframe = DisplacedChainedBonesTransformsFactory.get_displaced_transforms_for(
            bones_count=7,
            seed=2
        )

        animated_armature_tree_hierarchies = BlenderArmatureAnimator \
            .for_armature(blender_parented_armature_obj) \
            .animate_bone(name="E2_BONE_TOP",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[0],
                          keyframe_number=first_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_1",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[1],
                          keyframe_number=first_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_2",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[2],
                          keyframe_number=first_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_3",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[3],
                          keyframe_number=first_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_4",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[4],
                          keyframe_number=first_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_5",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[5],
                          keyframe_number=first_keyframe) \
            .animate_bone(name="E2_BONE_BOTTOM",
                          local_transform=displaced_chained_bones_transforms_first_keyframe[6],
                          keyframe_number=first_keyframe) \
                              \
                              \
            .animate_bone(name="E2_BONE_TOP",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[0],
                          keyframe_number=second_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_1",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[1],
                          keyframe_number=second_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_2",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[2],
                          keyframe_number=second_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_3",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[3],
                          keyframe_number=second_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_4",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[4],
                          keyframe_number=second_keyframe) \
            .animate_bone(name="E2_BONE_CHAIN_5",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[5],
                          keyframe_number=second_keyframe) \
            .animate_bone(name="E2_BONE_BOTTOM",
                          local_transform=displaced_chained_bones_transforms_second_keyframe[6],
                          keyframe_number=second_keyframe) \
            .commit()

        bone_animation_local_matrix_a = BlenderArmatureBoneCurrentAnimationDataHelper \
            .get_bone_local_matrix(
                armature=blender_parented_armature_obj, bone_name="E2_BONE_BOTTOM", frame_number=first_keyframe)

        bone_animation_local_matrix_b = BlenderArmatureBoneCurrentAnimationDataHelper \
            .get_bone_local_matrix(
                armature=blender_parented_armature_obj, bone_name="E2_BONE_BOTTOM", frame_number=second_keyframe)

        calculated_bone_animation_world_matrix_a = BoneMatrixHelper.get_world_matrix_for_bone(
                    "E2_BONE_BOTTOM", animated_armature_tree_hierarchies[0])  # type: Matrix4x4
        calculated_bone_animation_world_matrix_b = BoneMatrixHelper.get_world_matrix_for_bone(
                    "E2_BONE_BOTTOM", animated_armature_tree_hierarchies[1])  # type: Matrix4x4

        BlenderArmatureAnimator \
            .for_armature(blender_flat_armature_obj) \
            .animate_bone(
                 name="E1_BONE_BOTTOM",
                 local_transform=TransformNode.from_matrix4x4(calculated_bone_animation_world_matrix_a),
                 keyframe_number=first_keyframe) \
            .animate_bone(
                name="E1_BONE_BOTTOM",
                local_transform=TransformNode.from_matrix4x4(calculated_bone_animation_world_matrix_b),
                keyframe_number=second_keyframe) \
            .commit()

        raise NotImplementedError

    def _character_skeleton_animation_transformation_verification_example(self):
        raise NotImplementedError

    def execute(self):
        self._synthetic_transformation_verification_example()
        self._character_skeleton_animation_transformation_verification_example()
