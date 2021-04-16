from typing import Tuple
from bpy.types import Object
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode


class BlenderArmatureBuilder:
    def with_armature_name(self, armature_name: str) -> 'BlenderArmatureBuilder':
        raise NotImplementedError

    def with_bone(self, name: str, transform: TransformNode) -> 'BlenderArmatureBuilder':
        raise NotImplementedError

    def parent_bones(self, child: str, parent: str) -> 'BlenderArmatureBuilder':
        raise NotImplementedError

    def build(self) -> Tuple[Object, TreeHierarchy]:
        raise NotImplementedError
