from acbmc.blender_operations.blender_scene_manipulator import BlenderSceneManipulator
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute()))

from acbmc.blender_operations.model_build.max_builtin_blend_fbx_exp_comp_anim_char_const import \
 MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor
from acbmc.model.animated_character.constructing.animated_character_description_loader import AnimatedCharacterDescriptionLoader
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription

class ImportAnimatedCharacterLogic:
    def execute(self, filepath_to_import: str):
        animated_character_description = AnimatedCharacterDescriptionLoader().load(filepath_to_import)  # type: AnimatedCharacterDescription
        BlenderSceneManipulator().clear_scene()
        animated_character_constructor = MaxBuiltinBlenderFbxExportComplianceAnimatedCharacterConstructor()
        animated_character_constructor.construct_animated_character(animated_character_description)


if __name__ == '__main__':
    ImportAnimatedCharacterLogic().execute()
