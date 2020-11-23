import json
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription
from acbmc.model.animated_character.constructing.animated_character_description_factory import AnimatedCharacterDescriptionFactory, AnimatedCharacterDescriptionFactoryForTesting


class AnimatedCharacterDescriptionLoader:
    def __init__(self):
        self.animated_character_description_factory = AnimatedCharacterDescriptionFactory()

    def load(self, filepath: str) -> AnimatedCharacterDescription:
        with open(filepath, 'r') as animated_character_file_handle:
            json_dict = json.loads(animated_character_file_handle.read())
        return self.animated_character_description_factory.construct_from_json(json_dict)


class AnimatedCharacterDescriptionLoaderForTesting(AnimatedCharacterDescriptionLoader):
    def __init__(self):
        super().__init__()
        self.animated_character_description_factory = AnimatedCharacterDescriptionFactoryForTesting()
