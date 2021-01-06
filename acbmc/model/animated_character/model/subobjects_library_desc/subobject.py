from typing import Callable
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geometric_object import GeometricObject


class Subobject:
    def __init__(self):
        self.object_number = -1  # type: int
        self.geometric_object = GeometricObject()

    def contains_actual_bones(self) -> bool:
        return self.geometric_object.contains_actual_bones()

    def reform_space_model(
        self,
        position3d_transformation: Callable[[Vector3d], None],
        rotation_transformation: Callable[[Quaternion], None]):

        self.geometric_object.reform_space_model(
            position3d_transformation=position3d_transformation,
            rotation_transformation=rotation_transformation
        )