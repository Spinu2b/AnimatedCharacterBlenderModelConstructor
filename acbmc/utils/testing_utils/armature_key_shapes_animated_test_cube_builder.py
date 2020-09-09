from typing import List

from acbmc.utils.math.transform import Transform
from acbmc.utils.math.vector3d import Vector3d


class ArmatureKeyShapesAnimatedTestCubeBuilder:
    def set_bone_keyframe(self, frame: int, absolute_transform: Transform) -> 'ArmatureKeyShapesAnimatedTestCubeBuilder':
        raise NotImplementedError
        return self

    def set_keyshape(self, frame: int, vertices: List[Vector3d]) -> 'ArmatureKeyShapesAnimatedTestCubeBuilder':
        raise NotImplementedError
        return self

    def instantiate(self):
        raise NotImplementedError
