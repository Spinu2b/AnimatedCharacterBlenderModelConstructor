from typing import Dict


class MaterialDescription:
    def __init__(self):
        self.textures = dict()  # type: Dict[str, str]


class Material:
    def __init__(self):
        self.identifier = None  # type: str
        self.description = MaterialDescription()
