from typing import Dict
from acbmc.model.animated_character.model \
    .subobjects_library_desc.subobject import Subobject
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class BlenderEditModeArmatureModelFactory:
    def get_blender_edit_mode_armature_model(
        self, subobjects: Dict[int, Subobject]) -> TreeHierarchy:
        raise NotImplementedError
