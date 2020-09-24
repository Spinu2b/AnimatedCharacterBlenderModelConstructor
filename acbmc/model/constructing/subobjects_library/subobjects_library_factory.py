from acbmc.model.constructing.subobjects_library.subobjects_factory import SubobjectsFactory
from acbmc.model.constructing.subobjects_library.visual_data_factory import VisualDataFactory
from acbmc.model.model.subobjects_library import SubobjectsLibrary


class SubobjectsLibraryFactory:
    def construct_from_json_dict(self, subobjects_library_json_dict) -> SubobjectsLibrary:
        result = SubobjectsLibrary()
        result.visual_data = VisualDataFactory().construct_from_json_dict(subobjects_library_json_dict["visualData"])
        result.subobjects = SubobjectsFactory().construct_from_json_dict(subobjects_library_json_dict["subobjects"])
        return result
