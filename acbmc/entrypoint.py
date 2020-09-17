import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute()))

from acbmc.model.constructing.animated_character_description_loader import AnimatedCharacterDescriptionLoader
from acbmc.model.model.animated_character_description import AnimatedCharacterDescription
from acbmc.blender_operations.model_build.animated_character_factory import AnimatedCharacterFactory

class ImportAnimatedCharacterLogic:
    def execute(self, filepath_to_import: str):
        animated_character_description = AnimatedCharacterDescriptionLoader().load(filepath_to_import)  # type: AnimatedCharacterDescription
        AnimatedCharacterFactory().build_animated_character(animated_character_description)


if __name__ == '__main__':
    ImportAnimatedCharacterLogic().execute()
