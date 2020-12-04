

class SubobjectsRelatedDataNamingHelper:
    @staticmethod
    def get_subobject_name(subobject_number: int) -> str:
        return "SUBOBJECT_{}".format(subobject_number)

    @staticmethod
    def get_duplicated_material_instance_name(subobject_number: int, material_identifier: str) -> str:
        raise NotImplementedError

    @staticmethod
    def get_duplicated_image_instance_name(
        subobject_number: int,
        material_identifier: str,
        texture_identifier: str,
        image_identifier: str) -> str:
        raise NotImplementedError
