from typing import Iterator, Tuple
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip


class AnimationFramesIteratingHelper:
    @classmethod
    def iterate_appropriate_pose_armature_hierarchies_for_keyframes_setting(
        cls,
        animation_clip: AnimationClip,
        armature_bind_pose_hierarchy: TreeHierarchy) -> Iterator[Tuple[TreeHierarchy, int]]:
        raise NotImplementedError
