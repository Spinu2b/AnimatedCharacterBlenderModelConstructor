from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class TransformNode:
    def __init__(self):
        self.position = Vector3d()
        self.rotation = Quaternion()
        self.scale = Vector3d()

    @staticmethod
    def lerp(transform_a: 'TransformNode', transform_b: 'TransformNode', interpolation: float) -> 'TransformNode':
        result = TransformNode()
        result.position = Vector3d.lerp(transform_a.position, transform_b.position, interpolation)
        result.rotation = Quaternion.lerp(transform_a.rotation, transform_b.rotation, interpolation)
        result.scale = Vector3d.lerp(transform_a.scale, transform_b.scale, interpolation)
        return result
