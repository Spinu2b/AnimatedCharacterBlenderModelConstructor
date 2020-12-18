from typing import Optional, Tuple
from bpy.types import Armature, Object
from acbmc.blender_operations.model_build.builtin_blend_fbx_exp_comp \
    .constructing.blender_armature_generator import BlenderArmatureGenerator
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class BlenderArmatureConstructor:
    def build_armature(
        self,
        blender_edit_mode_armature_model: TreeHierarchy,
        name: str) -> Tuple[Armature, Object]:

        blender_armature_generator = BlenderArmatureGenerator()

        armature, armature_obj = blender_armature_generator.create_armature(name=name)
        for edit_mode_bone_node_iter in blender_edit_mode_armature_model.iterate_nodes():
            blender_armature_generator.place_bone(
                edit_mode_bone_node=edit_mode_bone_node_iter.node,
                armature=armature,
                armature_obj=armature_obj
            )

        for child_parent_pair in blender_edit_mode_armature_model.iterate_parent_child_key_pairs():
            parent_key = child_parent_pair[0]  # type: Optional[str]
            node_key = child_parent_pair[1]  # type: str

            if parent_key is not None:
                blender_armature_generator.parent_bone_to(
                    child=node_key,
                    parent=parent_key,
                    armature=armature
                )
        
        return armature, armature_obj
