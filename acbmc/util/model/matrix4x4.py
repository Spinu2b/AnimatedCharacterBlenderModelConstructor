from typing import List, Tuple
import mathutils
from acbmc.model.animated_character.model.math.quaternion import Quaternion
from acbmc.model.animated_character.model.math.vector3d import Vector3d


class Matrix4x4:
    def __init__(self):
        self.elements = [[0 for i in range(4)] for j in range(4)]  # type: List[List[int]]

    @staticmethod
    def identity_matrix() -> 'Matrix4x4':
        return Matrix4x4.from_blender_matrix(mathutils.Matrix.Identity(4))

    def decompose(self) -> Tuple[Vector3d, Quaternion, Vector3d]:
        bl_position, bl_rotation, bl_scale = self.to_blender_matrix().decompose()
        return Vector3d.from_blender_vector(bl_position), \
            Quaternion.from_blender_quaternion(bl_rotation), Vector3d.from_blender_vector(bl_scale)

    def copy(self) -> 'Matrix4x4':
        result = Matrix4x4()
        for i in range(4):
            for j in range(4):
                result.elements[i][j] = self.elements[i][j]
        return result

    @classmethod
    def from_blender_matrix(cls, matrix: mathutils.Matrix) -> 'Matrix4x4':
        result = Matrix4x4()
        for i in range(4):
            for j in range(4):
                result.elements[i][j] = matrix[i][j]
        return result

    def to_blender_matrix(self) -> mathutils.Matrix:
        result = mathutils.Matrix()
        for i in range(4):
            for j in range(4):
                result[i][j] = self.elements[i][j]
        return result

    def __mul__(self, other):
        a_matrix = self.to_blender_matrix()
        b_matrix = other.to_blender_matrix()
        return Matrix4x4.from_blender_matrix(a_matrix * b_matrix)

    def inverted(self) -> 'Matrix4x4':
        blender_matrix = self.to_blender_matrix()  # type: mathutils.Matrix
        return Matrix4x4.from_blender_matrix(blender_matrix.inverted())
