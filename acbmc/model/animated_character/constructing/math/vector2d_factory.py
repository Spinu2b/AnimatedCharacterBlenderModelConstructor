from acbmc.model.animated_character.model.math.vector2d import Vector2d


class Vector2DFactory:
    def construct_from_json_dict(self, vector2d_json_dict) -> Vector2d:
        result = Vector2d()
        result.x = vector2d_json_dict["x"]
        result.y = vector2d_json_dict["y"]
        return result
