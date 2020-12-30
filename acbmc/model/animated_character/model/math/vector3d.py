import mathutils

class Vector3d:
    def __init__(self, x: float=0.0, y: float=0.0, z: float=0.0):
        self.x = x  # type: float
        self.y = y  # type: float
        self.z = z  # type: float

    @staticmethod
    def from_blender_vector(vector: mathutils.Vector) -> 'Vector3d':
        return Vector3d(vector.x, vector.y, vector.z)

    def copy(self) -> 'Vector3d':
        return Vector3d(x=self.x, y=self.y, z=self.z)

    def lerp(vector3d_a: 'Vector3d', vector3d_b: 'Vector3d', interpolation: float) -> 'Vector3d':
        mathutils_vector_a = mathutils.Vector((vector3d_a.x, vector3d_a.y, vector3d_a.z))  
        mathutils_vector_b = mathutils.Vector((vector3d_b.x, vector3d_b.y, vector3d_b.z))

        interpolated_mathutils_vector = mathutils_vector_a.lerp(mathutils_vector_b, interpolation)  # type: mathutils.Vector
        return Vector3d(interpolated_mathutils_vector.x, interpolated_mathutils_vector.y, interpolated_mathutils_vector.z)

    def __add__(self, other: 'Vector3d') -> 'Vector3d':
        result = Vector3d()
        result.x = self.x + other.x
        result.y = self.y + other.y
        result.z = self.z + other.z
        return result
