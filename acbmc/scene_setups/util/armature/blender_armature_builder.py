from typing import Dict, List, Tuple
from bpy.types import Object
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from acbmc.util.model.transform_node import TransformNode


class BlenderArmatureBuilder:
    def __init__(self):
        self.armature_name = None  # type: str
        self.bones_edit_mode_transforms = []  # type: List[TransformNode]
        self.bones_parentings = dict()  # type: Dict[str, str]

    def with_armature_name(self, armature_name: str) -> 'BlenderArmatureBuilder':
        self.armature_name = armature_name
        return self

    def with_bone(self, name: str, transform: TransformNode) -> 'BlenderArmatureBuilder':
        self.bones_edit_mode_transforms.append(transform.copy())
        return self

    def parent_bones(self, child: str, parent: str) -> 'BlenderArmatureBuilder':
        self.bones_parentings[child] = parent
        return self

    def build(self) -> Tuple[Object, TreeHierarchy]:
        raise NotImplementedError
