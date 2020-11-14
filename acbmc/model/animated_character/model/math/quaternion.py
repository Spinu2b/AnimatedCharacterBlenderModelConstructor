import mathutils


class Quaternion:
    def __init__(self, w: float=1.0, x: float=0.0, y: float=0.0, z: float=0.0):
        self.w = w  # type: float
        self.x = x  # type: float
        self.y = y  # type: float
        self.z = z  # type: float

    def copy(self) -> 'Quaternion':
        return Quaternion(w=self.w, x=self.x, y=self.y, z=self.z)

    def lerp(quaternion_a: 'Quaternion', quaternion_b: 'Quaternion', interpolation: float) -> 'Quaternion':
        mathutils_quaternion_a = mathutils.Quaternion((quaternion_a.w, quaternion_a.x, quaternion_a.y, quaternion_a.z))
        mathutils_quaternion_b = mathutils.Quaternion((quaternion_b.w, quaternion_b.x, quaternion_b.y, quaternion_b.z))

        interpolated_mathutils_quaternion = \
            mathutils_quaternion_a.slerp(mathutils_quaternion_b, interpolation)  # type: mathutils.Quaternion

        return Quaternion(w=interpolated_mathutils_quaternion.w, x=interpolated_mathutils_quaternion.x, 
            y=interpolated_mathutils_quaternion.y, z=interpolated_mathutils_quaternion.z)
