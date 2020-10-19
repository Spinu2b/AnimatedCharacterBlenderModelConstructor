from typing import Any, Callable, Dict
from acbmc.util.CollectionsUtils import CollectionsUtils


class DictUtils:
    @staticmethod
    def extend_dict_with_duplicated_keys_errors(
        base_dict: Dict[Any, Any], extending_dict: Dict[Any, Any]):
        raise NotImplementedError
    
    @staticmethod
    def are_dicts_equal(
        dict_a: Dict[Any, Any], dict_b: Dict[Any, Any],
         value_comparison_lambda: Callable[[Any, Any], bool]) -> bool:
        
        if not CollectionsUtils.have_the_same_elements(dict_a.keys(), dict_b.keys()):
            return False

        for key in dict_a:
            value_a = dict_a[key]  # type: Any
            value_b = dict_b[key]  # type: Any

            if not value_comparison_lambda(value_a, value_b):
                return False

        return True
