from typing import Dict


class MaterialDescription:
    def __init__(self):
        self.textures = dict()  # type: Dict[str, str]


class Material:
    def __init__(self):
        self.identifier = None  # type: str
        self.description = MaterialDescription()

    def get_one_expected_texture_identifier_or_throw_exception_in_any_other_case(self) -> str:
        if len(self.description.textures) != 1:
            raise ValueError("Inproper amount of expected textures on the material! {}".format(len(self.description.textures)))

        return (list(self.description.textures.values()))[0]
