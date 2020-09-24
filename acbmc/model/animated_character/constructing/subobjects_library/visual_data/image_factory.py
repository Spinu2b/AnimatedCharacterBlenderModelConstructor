from typing import List
from acbmc.model.animated_character.model.subobjects_library_desc.image import Color, Image, ImageDescription


class ColorFactory:
    def construct_from_json_dict(self, color_json_dict) -> Color:
        result = Color()
        result.red = color_json_dict["red"]
        result.green = color_json_dict["green"]
        result.blue = color_json_dict["blue"]
        result.alpha = color_json_dict["alpha"]
        return result


class ImagePixelsFactory:
    def construct_from_json_dict(self, image_pixels_json_dict) -> List[Color]:
        result = []  # type: List[Color]
        color_factory = ColorFactory()
        for color_json_dict in image_pixels_json_dict:
            result.append(color_factory.construct_from_json_dict(color_json_dict))
        return result


class ImageDescriptionFactory:
    def construct_from_json_dict(self, image_description_json_dict) -> ImageDescription:
        result = ImageDescription()
        result.width = image_description_json_dict["width"]
        result.height = image_description_json_dict["height"]
        result.pixels = ImagePixelsFactory().construct_from_json_dict(image_description_json_dict["pixels"])
        return result


class ImageFactory:
    def construct_from_json_dict(self, image_json_dict) -> Image:
        result = Image()
        result.image_description_identifier = image_json_dict["imageDescriptionIdentifier"]
        result.image_description = ImageDescriptionFactory().construct_from_json_dict(image_json_dict["imageDescription"])
        return result
