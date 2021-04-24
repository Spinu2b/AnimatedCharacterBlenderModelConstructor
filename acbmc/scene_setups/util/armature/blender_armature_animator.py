from typing import Dict, List
from bpy.types import Object
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode


class BlenderArmatureAnimator:
    def __init__(self, blender_armature_obj: Object):
        self.blender_armature_obj = blender_armature_obj
        self.bones_keyframes = dict()  # type: Dict[int, Dict[str, TransformNode]]

    def _add_keyframe_if_does_not_exist(self, keyframe_number: int):
        if keyframe_number not in self.bones_keyframes:
            self.bones_keyframes[keyframe_number] = dict()

    @classmethod
    def for_armature(cls, blender_armature_obj: Object) -> 'BlenderArmatureAnimator':
        return BlenderArmatureAnimator(blender_armature_obj)

    def animate_bone(self, name: str, local_transform: TransformNode, keyframe_number: int) -> 'BlenderArmatureAnimator':
        self._add_keyframe_if_does_not_exist(keyframe_number)
        self.bones_keyframes[keyframe_number][name] = local_transform.copy()
        return self

    def commit(self) -> List[TreeHierarchy]:
        raise NotImplementedError
