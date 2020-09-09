from acbmc.utils.math.quaternion import Quaternion
from acbmc.utils.math.vector3d import Vector3d


class Transform:
    @classmethod
    def translate_by(cls, transform: 'Transform', offset: Vector3d) -> 'Transform':
        raise NotImplementedError


class TransformBuilder:
    def set_position(self, position: Vector3d) -> 'TransformBuilder':
        raise NotImplementedError
        return self

    def set_rotation(self, rotation: Quaternion) -> 'TransformBuilder':
        raise NotImplementedError
        return self

    def set_scale(self, scale: Vector3d) -> 'TransformBuilder':
        raise NotImplementedError
        return self

    def build(self) -> Transform:
        raise NotImplementedError
