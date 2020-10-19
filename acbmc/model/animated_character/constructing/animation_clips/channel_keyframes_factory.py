from acbmc.model.animated_character.constructing.math.quaternion_factory import QuaternionFactory
from acbmc.model.animated_character.constructing.math.vector3d_factory import Vector3dFactory
from typing import Dict
from acbmc.model.animated_character.model.animation_clips_desc.channel_transform import ChannelTransform


class ChannelTransformFactory:
    def construct_from_json_dict(self, channel_transform_json_dict) -> ChannelTransform:
        result = ChannelTransform()
        result.position = Vector3dFactory().construct_from_json_dict(channel_transform_json_dict["position"])
        result.rotation = QuaternionFactory().construct_from_json_dict(channel_transform_json_dict["rotation"])
        result.scale = Vector3dFactory().construct_from_json_dict(channel_transform_json_dict["scale"])
        return result

class ChannelKeyframesFactory:
    def construct_from_json_dict(self, channel_keyframes_json_dict) -> Dict[int, Dict[int, ChannelTransform]]:
        result = dict()  # type: Dict[int, Dict[int, ChannelTransform]]
        channel_transform_factory = ChannelTransformFactory()
        for channel_id_iter in channel_keyframes_json_dict:
            channel_id = int(channel_id_iter)
            result[channel_id] = dict()
            for frame_number_iter in channel_keyframes_json_dict[channel_id_iter]:
                frame_number = int(frame_number_iter)
                result[channel_id][frame_number] = \
                    channel_transform_factory.construct_from_json_dict(channel_keyframes_json_dict[channel_id_iter][frame_number_iter])
        return result
