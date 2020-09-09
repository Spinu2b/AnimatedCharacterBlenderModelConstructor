

class Vector3d:
    def __init__(self, x: float, y: float, z: float):
        self.x = x  # type: float
        self.y = y  # type: float
        self.z = z  # type: float

    def __mul__(self, other) -> 'Vector3d':
        raise NotImplementedError
