from typing import Dict
from acbmc.model.constructing.subobjects_library.visual_data.image_factory import ImageFactory
from acbmc.model.constructing.subobjects_library.visual_data.texture2d_factory import Texture2DFactory
from acbmc.model.constructing.subobjects_library.visual_data.material_factory import MaterialFactory
from acbmc.model.model.subobjects_library_desc.image import Image
from acbmc.model.model.subobjects_library_desc.texture2d import Texture2D
from acbmc.model.model.subobjects_library_desc.material import Material
from acbmc.model.model.subobjects_library_desc.visual_data import VisualData


class MaterialsFactory:
    def construct_from_json_dict(self, materials_json_dict) -> Dict[str, Material]:
        result = dict()  # type: Dict[str, Material]
        material_factory = MaterialFactory()
        for material_identifier in materials_json_dict:
            result[material_identifier] = material_factory.construct_from_json_dict(materials_json_dict[material_identifier])
        return result


class TexturesFactory:
    def construct_from_json_dict(self, textures_json_dict) -> Dict[str, Texture2D]:
        result = dict()  # type: Dict[str, Texture2D]
        texture2d_factory = Texture2DFactory()
        for texture2d_identifier in textures_json_dict:
            result[texture2d_identifier] = texture2d_factory.construct_from_json_dict(textures_json_dict[texture2d_identifier])
        return result


class ImagesFactory:
    def construct_from_json_dict(self, images_json_dict) -> Dict[str, Image]:
        result = dict()  # type: Dict[str, Image]
        image_factory = ImageFactory()
        for image_identifier in images_json_dict:
            result[image_identifier] = image_factory.construct_from_json_dict(images_json_dict[image_identifier])
        return result


class VisualDataFactory:
    def construct_from_json_dict(self, visual_data_json_dict) -> VisualData:
        result = VisualData()
        result.materials = MaterialsFactory().construct_from_json_dict(visual_data_json_dict["materials"])
        result.textures = TexturesFactory().construct_from_json_dict(visual_data_json_dict["textures"])
        result.images = ImagesFactory().construct_from_json_dict(visual_data_json_dict["images"])
        return result
