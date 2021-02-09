from typing import Dict, Iterator, List, Tuple
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .animations.pos_hierarch_for_subobj_usa_cons_trans import PoseHierarchiesForSubobjectsUsageConsolidationTransformer
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.uni_ani_clip_arm_tree_hier_with_def_sets_fetch import \
     UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class AnimationFramesIteratingHelper:
    @classmethod
    def iterate_appropriate_pose_armature_hierarchies_for_keyframes_setting(
        cls,
        animation_clip: AnimationClip,
        armature_bind_pose_hierarchy: TreeHierarchy,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: ChannelHierarchies,
        subobjects_channels_associations: SubobjectsChannelsAssociations) -> Iterator[Tuple[int, TreeHierarchy]]:

        armature_tree_hierarchies_fetcher = UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher()

        pose_hierarchies_in_animation_clip_infos = []  # type: List[Tuple[int, TreeHierarchy]]
        for frame_number, armature_tree_hierarchy_with_deform_sets_in_animation_clip in \
                armature_tree_hierarchies_fetcher.iterate_armature_hierarchies_with_deform_sets_for_animation_clip(
                    animation_clip=animation_clip, subobjects_dict=subobjects_dict,
                    channel_hierarchies=channel_hierarchies, subobjects_channels_associations=subobjects_channels_associations,
                    new_tree_hierarchy_for_each_keyframes_set_change=True):

            pose_hierarchies_in_animation_clip_infos.append((frame_number, armature_tree_hierarchy_with_deform_sets_in_animation_clip))
            
        PoseHierarchiesForSubobjectsUsageConsolidationTransformer \
            .analyze_and_transform_the_pose_hierarchies_list_considering_subobjects_usage_and_prepare_appropriately_keyframed_final_pose_armature_hierarchies(
                pose_hierarchies_in_animation_clip_infos, armature_bind_pose_hierarchy
            )    
        for pose_hierarchy_info in pose_hierarchies_in_animation_clip_infos:
            yield pose_hierarchy_info
