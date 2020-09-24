

from acbmc.model.animated_character.model.animation_clips_desc.animation_frames_period_info import AnimationFramesPeriodInfo


class AnimationFramesPeriodInfoFactory:
    def construct_from_json_dict(self, animation_frames_period_info_json_dict) -> AnimationFramesPeriodInfo:
        result = AnimationFramesPeriodInfo()
        result.frame_begin = animation_frames_period_info_json_dict["frameBegin"]
        result.frame_end = animation_frames_period_info_json_dict["frameEnd"]
        return result 
