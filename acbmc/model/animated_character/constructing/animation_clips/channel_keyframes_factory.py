from typing import Dict
from acbmc.model.animated_character.model.math.vector3d import Vector3d
from acbmc.util.model.transform_node import TransformNode
from acbmc.model.animated_character.constructing.math.quaternion_factory import QuaternionFactory
from acbmc.model.animated_character.constructing.math.vector3d_factory import Vector3dFactory


class ChannelTransformFactory:
    def construct_from_json_dict(self, channel_transform_json_dict) -> TransformNode:
        result = TransformNode()
        result.position = Vector3dFactory().construct_from_json_dict(channel_transform_json_dict["position"])

        # altered_position = Vector3d(-result.position.x, -result.position.z, result.position.y) 
        # result.position = altered_position

        result.rotation = QuaternionFactory().construct_from_json_dict(channel_transform_json_dict["rotation"])
        result.scale = Vector3dFactory().construct_from_json_dict(channel_transform_json_dict["scale"])
        return result

class ChannelKeyframesFactory:
    def construct_from_json_dict(self, channel_keyframes_json_dict) -> Dict[int, Dict[int, TransformNode]]:
        result = dict()  # type: Dict[int, Dict[int, TransformNode]]
        channel_transform_factory = ChannelTransformFactory()
        for channel_id_iter in channel_keyframes_json_dict:
            channel_id = int(channel_id_iter)
            result[channel_id] = dict()
            for frame_number_iter in channel_keyframes_json_dict[channel_id_iter]:
                frame_number = int(frame_number_iter)
                result[channel_id][frame_number] = \
                    channel_transform_factory.construct_from_json_dict(channel_keyframes_json_dict[channel_id_iter][frame_number_iter])
        return result
