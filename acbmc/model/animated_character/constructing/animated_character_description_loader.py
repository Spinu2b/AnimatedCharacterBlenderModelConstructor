import json
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.animated_character.constructing.animated_character_description_factory import AnimatedCharacterDescriptionFactory


class AnimatedCharacterDescriptionLoader:
    def load(self, filepath: str) -> AnimatedCharacterDescription:
        with open(filepath, 'r') as animated_character_file_handle:
            json_dict = json.loads(animated_character_file_handle.read())
        return AnimatedCharacterDescriptionFactory().construct_from_json(json_dict)
