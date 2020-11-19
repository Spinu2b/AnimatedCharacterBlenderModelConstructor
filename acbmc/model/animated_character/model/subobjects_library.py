from typing import Dict
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.subobjects_library_desc.visual_data import VisualData


class SubobjectsLibrary:
    def __init__(self):
        self.visual_data = VisualData()
        self.subobjects = dict()  # type: Dict[int, Subobject]
