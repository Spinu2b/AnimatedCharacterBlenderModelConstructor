from typing import Dict
from acbmc.blender_operations \
    .model_build.builtin_blend_fbx_exp_comp \
    .armature.building.node_trav_impls.subobj_bon_on_arm_mod_build_impl import SubobjectsBonesOnlyArmatureModelBuilderImplementation
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class WithChannelsBonesArmatureModelBuilderImplementation(SubobjectsBonesOnlyArmatureModelBuilderImplementation):
    def get_blender_armature_model(self, data: any) -> TreeHierarchy:
        subobjects = data[0]  # type: Dict[int, Subobject]

        base_model = super().get_blender_armature_model(subobjects)

        raise NotImplementedError
