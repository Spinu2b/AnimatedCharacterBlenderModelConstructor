from typing import Tuple
from bpy.types import Armature, Object


class BlenderArmatureGenerator:
    def create_armature(self, name: str) -> Tuple[Armature, Object]:
        blender_armature_manipulator = BlenderArmatureManipulator()
        return blender_armature_manipulator.create_armature(name=name)
