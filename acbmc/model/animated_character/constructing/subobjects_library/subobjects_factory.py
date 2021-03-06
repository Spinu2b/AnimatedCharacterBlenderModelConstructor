from typing import Dict
from acbmc.model.animated_character.constructing.subobjects_library.subobjects.geometric_object_factory import GeometricObjectFactory
from acbmc.model.animated_character.model.subobjects_library_desc.subobject_desc.geometric_object import GeometricObject
from acbmc.model.animated_character.model.subobjects_library_desc.subobject import Subobject

class SubobjectFactory:
    def construct_from_json_dict(self, subobject_json_dict) -> Subobject:
        result = Subobject()
        result.object_number = int(subobject_json_dict["objectNumber"])
        result.geometric_object = GeometricObjectFactory().construct_from_json_dict(subobject_json_dict["geometricObject"])
        return result


class SubobjectsFactory:
    def construct_from_json_dict(self, subobjects_json_dict) -> Dict[int, Subobject]:
        result = dict()  # type: Dict[int, Subobject]
        subobject_factory = SubobjectFactory()
        for subobject_number_iter in subobjects_json_dict:
            subobject_number = int(subobject_number_iter)
            result[subobject_number] = subobject_factory.construct_from_json_dict(subobjects_json_dict[subobject_number_iter])
        return result
