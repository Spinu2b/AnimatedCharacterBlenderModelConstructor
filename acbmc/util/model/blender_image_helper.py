from typing import List
import array
import bpy
from bpy.types import Image
from acbmc.model.animated_character.model.subobjects_library_desc.image import Color


class BlenderImageHelper:
    def get_blender_image(
        self,
        width: int,
        height: int,
        image_name: str,
        texture_image_definition: List[Color]) -> Image:
        blender_image = bpy.data.images.new(name=image_name, width=width, height=height, alpha=True)  # type: Image
        pixel_index = 0
        pixels_array = array.array('f', (0,)*len(texture_image_definition) * 4)
        for pixel_color in texture_image_definition:
            pixels_array[pixel_index] = pixel_color.red
            pixels_array[pixel_index + 1] = pixel_color.green
            pixels_array[pixel_index + 2] = pixel_color.blue
            pixels_array[pixel_index + 3] = pixel_color.alpha
            pixel_index += 4

        blender_image.pixels = pixels_array.tolist()
        blender_image.pack()
        return blender_image
