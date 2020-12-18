

from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geometric_object import GeometricObject


class Subobject:
    def __init__(self):
        self.object_number = -1  # type: int
        self.geometric_object = GeometricObject()

    def contains_actual_bones(self) -> bool:
        return self.geometric_object.contains_actual_bones()
