from abc import ABC, abstractmethod
from typing import Any
from acbmc.util.model.transform_node import TransformNode

class BoneNodesFactory(ABC):
    @abstractmethod
    def get_appropriate_subobject_actual_bone_node(self, bone_bind_pose: TransformNode, bone_name: str) -> Any:
        raise ValueError

    @abstractmethod
    def get_appropriate_subobject_parent_bone_node(self, bone_name: str) -> Any:
        raise ValueError
