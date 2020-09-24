from typing import Dict
from acbmc.model.animated_character.model.subobjects_library_desc.material import Material, MaterialDescription


class MaterialTexturesFactory:
    def construct_from_json_dict(self, material_textures_json_dict) -> Dict[str, str]:
        result = dict()  # type: Dict[str, str]
        for texture_name in material_textures_json_dict:
            result[texture_name] = material_textures_json_dict[texture_name]
        return result


class MaterialDescriptionFactory:
    def construct_from_json_dict(self, material_description_json_dict) -> MaterialDescription:
        result = MaterialDescription()
        result.textures = MaterialTexturesFactory().construct_from_json_dict(material_description_json_dict["textures"])
        return result


class MaterialFactory:
    def construct_from_json_dict(self, material_json_dict) -> Material:
        result = Material()
        result.identifier = material_json_dict["identifier"]
        result.description = MaterialDescriptionFactory().construct_from_json_dict(material_json_dict["description"])
        return result
