from acbmc.utils.math.quaternion import Quaternion
from acbmc.utils.math.vector3d import Vector3d


class Transform:
    def __init__(self):
        self.position = Vector3d(0.0, 0.0, 0.0)
        self.rotation = Quaternion(1.0, 0.0, 0.0, 0.0)
        self.scale = Vector3d(0.0, 0.0, 0.0)

    @classmethod
    def translate_by(cls, transform: 'Transform', offset: Vector3d) -> 'Transform':
        raise NotImplementedError


class TransformBuilder:
    def __init__(self):
        self.result = Transform()

    def set_position(self, position: Vector3d) -> 'TransformBuilder':
        self.result.position = position
        return self

    def set_rotation(self, rotation: Quaternion) -> 'TransformBuilder':
        self.result.rotation = rotation
        return self

    def set_scale(self, scale: Vector3d) -> 'TransformBuilder':
        self.result.scale = scale
        return self

    def build(self) -> Transform:
        return self.result
