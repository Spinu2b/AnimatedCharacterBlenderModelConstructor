from typing import Iterator
from acbmc.model.animated_character.constructing.animation_clips.animation_clip_factory import AnimationClipFactory
from acbmc.model.animated_character.model.animation_clips_desc.animation_clip import AnimationClip
from acbmc.model.animated_character.model.animation_clips import AnimationClips


class AnimationClipsJsonDictHelper:
    def iterate_animation_clip_objs(self, animation_clips_json_dict) -> Iterator[AnimationClip]:
        animation_clip_factory = AnimationClipFactory()
        for animation_clip_id in animation_clips_json_dict["animationClips"]:
            yield animation_clip_factory.construct_from_json_dict(animation_clips_json_dict["animationClips"][animation_clip_id])


class AnimationClipsJsonDictHelperForTesting(AnimationClipsJsonDictHelper):
    def iterate_animation_clip_objs(self, animation_clips_json_dict) -> Iterator[AnimationClip]:
        animation_clip_factory = AnimationClipFactory()
        current_animation_clip_id = 1
        for animation_clip_id in animation_clips_json_dict["animationClips"]:
            yield animation_clip_factory.construct_from_json_dict(animation_clips_json_dict["animationClips"][animation_clip_id])
            current_animation_clip_id += 1
            if current_animation_clip_id > 1:
                break


class AnimationClipsFactory:
    def __init__(self):
        self.animation_clips_json_dict_helper = AnimationClipsJsonDictHelper()

    def construct_from_json_dict(self, animation_clips_json_dict) -> AnimationClips:
        result = AnimationClips()
        for animation_clip in self.animation_clips_json_dict_helper.iterate_animation_clip_objs(animation_clips_json_dict):
            result.animation_clips[animation_clip.id] = animation_clip
        return result


class AnimationClipsFactoryForTesting(AnimationClipsFactory):
    def __init__(self):
        super().__init__()
        self.animation_clips_json_dict_helper = AnimationClipsJsonDictHelperForTesting()
