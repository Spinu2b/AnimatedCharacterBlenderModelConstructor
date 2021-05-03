from typing import List
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class ChainedBonesTransformsFactory:
    @classmethod
    def get_armature_chained_bones_transforms_for(
        cls, bones_count: int) -> List[TransformNode]:

        result = []  # type: List[TransformNode]

        current_position = Vector3d()
        home_rotation = Quaternion()
        home_scale = Vector3d(1.0, 1.0, 1.0)
        for _ in range(bones_count):
            current_position += Vector3d(x=0.0, y=1.0, z=0.0)
            result.append(TransformNode.construct_with(
                position=current_position, rotation=home_rotation, scale=home_scale))
        
        return result
