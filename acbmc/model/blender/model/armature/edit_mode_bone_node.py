from acbmc.model.animated_character.model.math.vector3d import Vector3d


class EditModeBoneNode:
    def __init__(self):
        self.bone_name = None  # type: str
        self.head_position = Vector3d()
        self.tail_position = Vector3d()
