import random
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from typing import List
from acbmc.util.model.transform_node import TransformNode
from mathutils import Quaternion


class DisplacedChainedBonesTransformsFactory:
  @classmethod
  def get_displaced_transforms_for(cls, bones_count: int, seed: int) -> List[TransformNode]:
    random.seed(seed)
    displaced_coordinates = [random.uniform(-1.0, 1.0) for _ in range(bones_count)]
    displaced_scale_coordinates = [random.uniform(0.5, 1.2) for _ in range(bones_count)]

    result = []  # type: List[TransformNode]
    home_rotation = Quaternion()

    for index in range(bones_count):
      result.append(
        TransformNode.construct_with(
          position=Vector3d(displaced_coordinates[index], displaced_coordinates[index], displaced_coordinates[index]),
          rotation=home_rotation,
          scale=Vector3d(displaced_scale_coordinates[index], displaced_scale_coordinates[index], displaced_scale_coordinates[index])
        )
      )

    return result
