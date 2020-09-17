

from acbmc.model.model.animated_character_description import AnimatedCharacterDescription


class AnimatedCharacterFactory:
    def build_animated_character(self, animated_character_description: AnimatedCharacterDescription):
        raise NotImplementedError
