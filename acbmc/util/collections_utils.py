import collections
from typing import Any, Collection, List


class CollectionsUtils:
    @staticmethod
    def have_the_same_elements(collection_a: Collection, collection_b: Collection) -> bool:
        return collections.Counter(collection_a) == collections.Counter(collection_b)

    @staticmethod
    def iterate_collection_and_return_copied_list(collection_obj: Any) -> List[Any]:
        result = []
        for elem in collection_obj:
            result.append(elem)
        return result
