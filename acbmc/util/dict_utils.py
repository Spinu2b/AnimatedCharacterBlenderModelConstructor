from typing import Any, Callable, Dict
from acbmc.util.collections_utils import CollectionsUtils


class DictUtils:
    @classmethod
    def have_common_keys(cls, dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> bool:
        keys_set_a = set(dict_a)
        keys_set_b = set(dict_b)

        return len(keys_set_a.intersection(keys_set_b)) != 0

    @classmethod
    def extend_dict_with_duplicated_keys_errors(
        cls,
        base_dict: Dict[Any, Any], extending_dict: Dict[Any, Any]):
        
        if cls.have_common_keys(base_dict, extending_dict):
            raise ValueError("Dicts share common keys! Will not extend.")

        base_dict.update(extending_dict)
    
    @classmethod
    def are_dicts_equal(cls,
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
