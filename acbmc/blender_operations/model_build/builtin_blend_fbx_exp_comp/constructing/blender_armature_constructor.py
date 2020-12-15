from typing import Tuple
from acbmc.util.model.tree_hierarchy import TreeHierarchy
from bpy.types import Armature, Object


class BlenderArmatureConstructor:
    def build_armature(
        self,
        blender_edit_mode_armature_model: TreeHierarchy,
        name: str) -> Tuple[Armature, Object]:
        raise NotImplementedError
