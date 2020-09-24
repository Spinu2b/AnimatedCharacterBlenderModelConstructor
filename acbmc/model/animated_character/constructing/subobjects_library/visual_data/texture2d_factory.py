from acbmc.model.animated_character.model.subobjects_library_desc.texture2d import Texture2D


class Texture2DFactory:
    def construct_from_json_dict(self, texture2d_json_dict) -> Texture2D:
        result = Texture2D()
        result.texture_description_identifier = texture2d_json_dict["textureDescriptionIdentifier"]
        result.image_identifier = texture2d_json_dict["imageIdentifier"]
        return result