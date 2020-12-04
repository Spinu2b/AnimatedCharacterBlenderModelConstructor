from typing import Dict, Tuple
from bpy.types import Armature, Object
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class BlenderSkinnedObjectsWithArmatureFactory:
    @classmethod
    def build_armature_considering_skinned_subobjects_and_target_bind_pose_model(
        cls,
        subobjects: Dict[int, Subobject],
        subobjects_mesh_objects: Dict[int, Object],
        armature_bind_pose_model: TreeHierarchy,
        armature_name: str) -> Tuple[Armature, Object]:

        raise NotImplementedError
