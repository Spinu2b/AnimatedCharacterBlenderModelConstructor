import collections
from typing import Collection


class CollectionsUtils:
    @staticmethod
    def have_the_same_elements(collection_a: Collection, collection_b: Collection) -> bool:
        return collections.Counter(collection_a) == collections.Counter(collection_b)
