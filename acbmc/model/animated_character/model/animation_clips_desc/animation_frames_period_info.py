

class AnimationFramesPeriodInfo:
    def __init__(self):
        self.frame_begin = 0  # type: int
        self.frame_end = 0  # type: int

    def contains_frame_number(self, frame_number: int) -> bool:
        return self.frame_begin < frame_number < self.frame_end
