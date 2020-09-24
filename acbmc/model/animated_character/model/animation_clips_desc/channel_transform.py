from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class ChannelTransform:
    def __init__(self):
        self.position = Vector3d(x=0.0, y=0.0, z=0.0)  # type: Vector3d
        self.rotation = Quaternion(w=1.0, x=0.0, y=0.0, z=0.0)  # type: Quaternion
        self.scale = Vector3d(x=1.0, y=1.0, z=1.0)  # type: Vector3d
