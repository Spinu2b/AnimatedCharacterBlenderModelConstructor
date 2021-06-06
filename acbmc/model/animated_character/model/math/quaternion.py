import math
import mathutils


class Quaternion:
    def __init__(self, w: float=1.0, x: float=0.0, y: float=0.0, z: float=0.0):
        self.w = w  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.z = z  # type: float

    def normalized(self) -> 'Quaternion':
        magnitude = self.abs()  # type: float
        return Quaternion(w=self.w / magnitude, x=self.x / magnitude, y=self.y / magnitude, z=self.z / magnitude)

    def copy(self) -> 'Quaternion':
        return Quaternion(w=self.w, x=self.x, y=self.y, z=self.z)

    def abs(self) -> float:
        return math.sqrt(self.w*self.w + self.x*self.x + self.y*self.y + self.z*self.z)

    def __sub__(self, other) -> 'Quaternion':
        result = Quaternion(
            w=self.w - other.w,
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )
        return result

    @staticmethod
    def from_blender_quaternion(quaternion: mathutils.Quaternion) -> 'Quaternion':
        return Quaternion(quaternion.w, quaternion.x, quaternion.y, quaternion.z)

    def lerp(quaternion_a: 'Quaternion', quaternion_b: 'Quaternion', interpolation: float) -> 'Quaternion':
        mathutils_quaternion_a = mathutils.Quaternion((quaternion_a.w, quaternion_a.x, quaternion_a.y, quaternion_a.z))
        mathutils_quaternion_b = mathutils.Quaternion((quaternion_b.w, quaternion_b.x, quaternion_b.y, quaternion_b.z))

        interpolated_mathutils_quaternion = \
            mathutils_quaternion_a.slerp(mathutils_quaternion_b, interpolation)  # type: mathutils.Quaternion

        return Quaternion(w=interpolated_mathutils_quaternion.w, x=interpolated_mathutils_quaternion.x, 
            y=interpolated_mathutils_quaternion.y, z=interpolated_mathutils_quaternion.z)

    def __mul__(self, other) -> 'Quaternion':
        return Quaternion.from_blender_quaternion(
            mathutils.Quaternion((self.w, self.x, self.y, self.z)) * mathutils.Quaternion((other.w, other.x, other.y, other.z)))
