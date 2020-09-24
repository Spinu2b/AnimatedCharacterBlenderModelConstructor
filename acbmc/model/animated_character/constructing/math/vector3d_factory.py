from acbmc.model.animated_character.model.math.vector3d import Vector3d


class Vector3dFactory:
    def construct_from_json_dict(self, vector3d_json_dict) -> Vector3d:
        result = Vector3d()
        result.x = vector3d_json_dict["x"]
        result.y = vector3d_json_dict["y"]
        result.z = vector3d_json_dict["z"]
        return result
