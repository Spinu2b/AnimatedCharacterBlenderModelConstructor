from acbmc.utils.math.vector3d import Vector3d


class SpaceModel:
    def get_forward_vector(self) -> Vector3d:
        raise NotImplementedError


class SpaceModels:
    @classmethod
    def get_blender_space_model(cls) -> 'SpaceModel':
        raise NotImplementedError
