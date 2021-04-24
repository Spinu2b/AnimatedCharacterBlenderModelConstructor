from typing import List
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class ChainedBonesTransformsFactory:
    @classmethod
    def get_armature_chained_bones_transforms_for(
        cls, bones_count: int, armature_position_offset_from_space_origin: Vector3d) -> List[TransformNode]:
        raise NotImplementedError
