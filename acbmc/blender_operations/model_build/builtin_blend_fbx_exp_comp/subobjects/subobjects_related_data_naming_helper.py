

class SubobjectsRelatedDataNamingHelper:
    @staticmethod
    def get_subobject_name(subobject_number: int) -> str:
        return "SUBOBJECT_{}".format(subobject_number)

    @staticmethod
    def get_duplicated_material_instance_name(subobject_number: int, material_identifier: str) -> str:
        return "MAT_SUBOBJECT_{}_MATERIAL_{}".format(subobject_number, material_identifier)

    @staticmethod
    def get_duplicated_image_instance_name(
        subobject_number: int,
        material_identifier: str,
        texture_identifier: str,
        image_identifier: str) -> str:

        return "IMG_SUBOBJECT_{}_MATERIAL_{}_TEXTURE_{}_IMAGE_{}".format(
            subobject_number, material_identifier, texture_identifier, image_identifier)

    @staticmethod
    def get_uv_layer_name(
        subobject_number: int,
        material_identifier: str,
        texture_identifier: str,
        image_identifier: str
    ) -> str:
        return "UV_SUBOBJECT_{}_MATERIAL_{}_TEXTURE_{}_IMAGE_{}".format(
            subobject_number, material_identifier, texture_identifier, image_identifier
        )
