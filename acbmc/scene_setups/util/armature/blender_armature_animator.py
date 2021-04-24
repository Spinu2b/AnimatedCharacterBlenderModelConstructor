from typing import List
from bpy.types import Object
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode


class BlenderArmatureAnimator:
    @classmethod
    def for_armature(blender_armature_obj: Object) -> 'BlenderArmatureAnimator':
        raise NotImplementedError

    def animate_bone(name: str, local_transform: TransformNode, keyframe_number: int) -> 'BlenderArmatureAnimator':
        raise NotImplementedError

    def commit(self) -> List[TreeHierarchy]:
        raise NotImplementedError
