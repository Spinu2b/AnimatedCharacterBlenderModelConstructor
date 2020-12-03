from typing import Dict
from acbmc.model.animated_character.model.subobjects_library_desc.image import Image
from acbmc.model.animated_character.model.subobjects_library_desc.texture2d import Texture2D
from acbmc.model.animated_character.model.subobjects_library_desc.material import Material


class VisualData:
    def __init__(self):
        self.materials = dict()  # type: Dict[str, Material]
        self.textures = dict()  # type: Dict[str, Texture2D]
        self.images = dict()  # type: Dict[str, Image]
