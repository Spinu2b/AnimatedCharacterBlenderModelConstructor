from acbmc.model.model.math.quaternion import Quaternion


class QuaternionFactory:
    def construct_from_json_dict(self, quaternion_json_dict) -> Quaternion:
        result = Quaternion()
        result.w = quaternion_json_dict["w"]
        result.x = quaternion_json_dict["x"]
        result.y = quaternion_json_dict["y"]
        result.z = quaternion_json_dict["z"]
        return result
