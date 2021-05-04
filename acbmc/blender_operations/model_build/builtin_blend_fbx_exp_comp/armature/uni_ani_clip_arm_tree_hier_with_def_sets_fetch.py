from typing import Dict, Iterator, List, Set, Tuple
from acbmc.blender_operations.model_build \
    .builtin_blend_fbx_exp_comp.armature.helpers.chan_tran_mono_analyzer import ChannelTransformsMonotonyAnalyzer
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.helpers.anim_fram_tree_mono_analyzer import AnimationFramesTreesMonotonyAnalyzer
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .armature.channels.uni_chan_arm_tree_hierarch_keyfr_fill import ChannelKeyframesHelper
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp.armature \
    .uni_arm_tree_hierarch_factory import UnifiedArmatureTreeHierarchyFactory
from acbmc.util.model.anim_clip.animation_clip_data_comparison_helper import AnimationClipDataComparisonHelper
from acbmc.util.model.anim_clip.anim_clip_model_parts_fetch_helper import AnimationClipModelPartsFetchingHelper
from acbmc.model.animated_character.model.subobjects_channels_associations_desc \
    .subobjects_channels_association import SubobjectsChannelsAssociation
from acbmc.model.animated_character.model.channel_hierarchies_desc.channel_hierarchy import ChannelHierarchy
from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo
from acbmc.model.animated_character.model.subobjects_channels_associations import SubobjectsChannelsAssociations
from acbmc.model.animated_character.model.channel_hierarchies import ChannelHierarchies
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class ArmatureTreeHierarchiesIteratingHelper:
    def iterate_armature_hierarchies_for(
        self,
        frames_count: int,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: Dict[str, ChannelHierarchy],
        channel_keyframes: Dict[int, Dict[int, TransformNode]],
        subobjects_channels_associations: Dict[str, SubobjectsChannelsAssociation],
        channels_for_subobjects_associations_data: Dict[str, List[AnimationFramesPeriodInfo]],
        animation_hierarchies: Dict[str, List[AnimationFramesPeriodInfo]],
        new_tree_hierarchy_for_each_keyframes_set_change: bool
    ) -> Iterator[Tuple[int, TreeHierarchy]]:
        animation_frames_trees_monotony_analyzer = AnimationFramesTreesMonotonyAnalyzer()
        channel_transforms_monotony_analyzer = ChannelTransformsMonotonyAnalyzer()
    
        first_frame_number = 0
        previous_channels_set = \
            AnimationClipModelPartsFetchingHelper.get_channels_set_for_frame(
                frame_number=first_frame_number,
                channel_keyframes=channel_keyframes)  # type: Set[int]
                #animation_hierarchies=animation_hierarchies,
                #channel_hierarchies=channel_hierarchies)  # type: Set[int]

        previous_channel_transforms = AnimationClipModelPartsFetchingHelper.get_channel_transforms_for_frame(
            frame_number=first_frame_number,
            frames_count=frames_count,
            channel_keyframes=channel_keyframes)  # Dict[int, TransformNode]

        previous_channels_for_subobjects_association = \
            AnimationClipModelPartsFetchingHelper.get_channels_for_subobjects_association_for_frame(
                frame_number=first_frame_number,
                channels_for_subobjects_associations_data=channels_for_subobjects_associations_data,
                subobjects_channels_associations=subobjects_channels_associations)  # type: SubobjectsChannelsAssociation

        previous_channel_hierarchy = AnimationClipModelPartsFetchingHelper.get_channel_hierarchy_for_frame(
            frame_number=first_frame_number,
            animation_hierarchies=animation_hierarchies,
            channel_hierarchies=channel_hierarchies)  # type: ChannelHierarchy

        given_tree_hierarchy = UnifiedArmatureTreeHierarchyFactory.derive_armature_tree_hierarchy_for(
            frame_number=first_frame_number,
            channel_hierarchy=previous_channel_hierarchy,
            channels_set=previous_channels_set,
            particular_frame_channel_transforms=previous_channel_transforms,
            channels_for_subobjects_association=previous_channels_for_subobjects_association,
            channel_keyframes=channel_keyframes,
            subobjects_dict=subobjects_dict)

        yield first_frame_number, given_tree_hierarchy

        animation_frames_trees_monotony_analyzer.consider_tree(given_tree_hierarchy)
        channel_transforms_monotony_analyzer.consider_channel_transforms(previous_channel_transforms)

        for frame_number in range(0, frames_count):
            current_channels_set = AnimationClipModelPartsFetchingHelper.get_channels_set_for_frame(
                frame_number=frame_number,
                channel_keyframes=channel_keyframes)  # type: Set[int]
                # animation_hierarchies=animation_hierarchies,
                # channel_hierarchies=channel_hierarchies)  # type: Set[int]

            current_channel_transforms = AnimationClipModelPartsFetchingHelper.get_channel_transforms_for_frame(
                frame_number=frame_number,
                frames_count=frames_count,
                channel_keyframes=channel_keyframes)  # type: Dict[int, TransformNode]

            channel_transforms_monotony_analyzer.consider_channel_transforms(current_channel_transforms)    

            current_channels_for_subobjects_association = \
                AnimationClipModelPartsFetchingHelper.get_channels_for_subobjects_association_for_frame(
                    frame_number=frame_number,
                    channels_for_subobjects_associations_data=channels_for_subobjects_associations_data,
                    subobjects_channels_associations=subobjects_channels_associations)  # type: SubobjectsChannelsAssociation

            current_channel_hierarchy = AnimationClipModelPartsFetchingHelper.get_channel_hierarchy_for_frame(
                frame_number=frame_number,
                animation_hierarchies=animation_hierarchies,
                channel_hierarchies=channel_hierarchies)  # type: ChannelHierarchy

            # If channels set changed between frames
            # OR
            # If channels to subobjects associations changed between frames
            # OR
            # If channels hierarchy changed between frames
            # THEN
            # Get new armature hierarchy that reflects that change
            if not AnimationClipDataComparisonHelper.are_channel_sets_equal(previous_channels_set, current_channels_set) or \
                not AnimationClipDataComparisonHelper.are_channels_for_subobjects_associations_equal(
                    previous_channels_for_subobjects_association, current_channels_for_subobjects_association) or \
                        not AnimationClipDataComparisonHelper.are_channel_hierarchies_equal(previous_channel_hierarchy, current_channel_hierarchy) or \
                        (frame_number != first_frame_number and \
                            new_tree_hierarchy_for_each_keyframes_set_change and \
                            ChannelKeyframesHelper.has_actual_keyframes_in_frame(frame_number, channel_keyframes)):

                        given_tree_hierarchy = UnifiedArmatureTreeHierarchyFactory.derive_armature_tree_hierarchy_for(
                            frame_number=frame_number,
                            channel_hierarchy=current_channel_hierarchy,
                            channels_set=current_channels_set,
                            particular_frame_channel_transforms=current_channel_transforms,
                            channels_for_subobjects_association=current_channels_for_subobjects_association,
                            channel_keyframes=channel_keyframes,
                            subobjects_dict=subobjects_dict)
                        yield frame_number, given_tree_hierarchy

                        animation_frames_trees_monotony_analyzer.consider_tree(given_tree_hierarchy)

            previous_channel_hierarchy = current_channel_hierarchy
            previous_channel_transforms = current_channel_transforms
            previous_channels_for_subobjects_association = current_channels_for_subobjects_association
            previous_channels_set = current_channels_set   

        channel_transforms_monotony_analyzer.raise_exception_if_monotonous()
        animation_frames_trees_monotony_analyzer.raise_exception_if_monotonous()         
        

class UnifiedAnimationClipArmatureTreeHierarchiesWithDeformSetsFetcher:
    def iterate_armature_hierarchies_with_deform_sets_for_animation_clip(
        self,
        animation_clip: AnimationClip,
        subobjects_dict: Dict[int, Subobject],
        channel_hierarchies: ChannelHierarchies,
        subobjects_channels_associations: SubobjectsChannelsAssociations,
        new_tree_hierarchy_for_each_keyframes_set_change: bool) -> Iterator[Tuple[int, TreeHierarchy]]:
        armature_tree_hierarchies_iterating_helper = ArmatureTreeHierarchiesIteratingHelper()
        yield from armature_tree_hierarchies_iterating_helper \
            .iterate_armature_hierarchies_for(
                frames_count=animation_clip.get_frames_count(),
                subobjects_dict=subobjects_dict,
                channel_hierarchies=channel_hierarchies.channel_hierarchies,
                channel_keyframes=animation_clip.channel_keyframes,
                subobjects_channels_associations=subobjects_channels_associations.subobjects_channels_associations,
                channels_for_subobjects_associations_data=animation_clip.channels_for_subobjects_associations_data,
                animation_hierarchies=animation_clip.animation_hierarchies,
                new_tree_hierarchy_for_each_keyframes_set_change=new_tree_hierarchy_for_each_keyframes_set_change
            )
