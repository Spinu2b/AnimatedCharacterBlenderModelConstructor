from typing import Callable, Dict
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject
from acbmc.model.animated_character.model.subobjects_library_desc.visual_data import VisualData


class SubobjectsLibrary:
    def __init__(self):
        self.visual_data = VisualData()
        self.subobjects = dict()  # type: Dict[int, Subobject]

    def reform_space_model(
        self,
        position3d_transformation: Callable[[Vector3d], None],
        rotation_transformation: Callable[[Quaternion], None]):

        for subobj in self.subobjects.values():
            subobj.reform_space_model(
                position3d_transformation=position3d_transformation,
                rotation_transformation=rotation_transformation
            )
