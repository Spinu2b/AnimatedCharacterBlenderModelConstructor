from acbmc.model.model.subobjects_library import SubobjectsLibrary


class SubobjectsLibraryFactory:
    def construct_from_json_dict(self, subobjects_library_json_dict) -> SubobjectsLibrary:
        raise NotImplementedError
