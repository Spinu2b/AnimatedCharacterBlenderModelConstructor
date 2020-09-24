from abc import ABC, abstractmethod
from acbmc.model.animated_character.model.animated_character_description import AnimatedCharacterDescription


class AnimatedCharacterConstructor(ABC):
    @abstractmethod
    def construct_animated_character(self, animated_character_description: AnimatedCharacterDescription):
        raise NotImplementedError
