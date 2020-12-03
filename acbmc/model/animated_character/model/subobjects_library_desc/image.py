from typing import List


class Color:
    def __init__(self):
        self.red = 0.0  # type: float
        self.green = 0.0  # type: float
        self.blue = 0.0  # type: float
        self.alpha = 0.0  # type: float


class ImageDescription:
    def __init__(self):
        self.width = 0  # type: int
        self.height = 0  # type: int
        self.pixels = []  # type: List[Color]


class Image:
    def __init__(self):
        self.image_description_identifier = None  # type: str
        self.image_description = ImageDescription()
