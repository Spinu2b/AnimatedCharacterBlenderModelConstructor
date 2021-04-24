from typing import List
from acbmc.util.model.transform_node import TransformNode


class DisplacedChainedBonesTransformsFactory:
  @classmethod
  def get_displaced_transforms_for(cls, bones_count: int, seed: int) -> List[TransformNode]:
    raise NotImplementedError
