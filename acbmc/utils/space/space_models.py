from abc import abstractmethod
from acbmc.utils.math.vector3d import Vector3d


class SpaceModel:
    @abstractmethod
    def get_forward_vector(self) -> Vector3d:
        raise NotImplementedError


class BlenderSpaceModel(SpaceModel):
    def get_forward_vector(self) -> Vector3d:
        return Vector3d(1.0, 0.0, 0.0)


class SpaceModels:
    @classmethod
    def get_blender_space_model(cls) -> 'SpaceModel':
        return BlenderSpaceModel()
