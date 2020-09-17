from acbmc.model.model.animation_clips import AnimationClips

class AnimationClipsFactory:
    def construct_from_json_dict(self, animation_clips_json_dict) -> AnimationClips:
        raise NotImplementedError
