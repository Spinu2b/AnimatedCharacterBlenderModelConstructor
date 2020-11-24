from typing import Any, Callable, Iterator, List, Optional, Sequence


class TreeIterationHelper:
    @classmethod
    def _traverse(
        cls,
        parent_element_key: Optional[Any],
        collection: Sequence[Any],
        parent_key_getter: Callable[[Any], Optional[Any]],
        node_key_getter: Callable[[Any], Any]
        ) -> Iterator[Any]:
        root_elements = [element for element in collection if parent_key_getter(element) == parent_element_key]
        for root_elem in root_elements:
            yield root_elem
            # root_element_children_list = [element for element in collection \
            #    if parent_key_getter(element) == node_key_getter(root_elem)]
            yield from cls._traverse(
                parent_element_key=node_key_getter(root_elem),
                collection=collection,
                parent_key_getter=parent_key_getter,
                node_key_getter=node_key_getter
            )

    @classmethod
    def iterate_sequence_in_order_of_tree_building(
        cls,
        collection: Sequence[Any],
        parent_key_getter: Callable[[Any], Optional[Any]],
        node_key_getter: Callable[[Any], Any]) -> Iterator[Any]:
        yield from cls._traverse(
            parent_element_key=None,
            collection=collection,
            parent_key_getter=parent_key_getter,
            node_key_getter=node_key_getter
        )
