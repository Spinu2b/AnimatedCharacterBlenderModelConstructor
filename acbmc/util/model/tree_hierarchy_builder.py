from typing import Any, Optional
from acbmc.util.model.tree_hierarchy import TreeHierarchy


class TreeHierarchyBuilder:
    def __init__(self):
        self._tree_building_blocks = []  # List[Tuple[Optional[Any], Any, Any]]

    def add_node(self, parent_key: Optional[Any], key: Any, node: Any) -> 'TreeHierarchyBuilder':
        self._tree_building_blocks.append((parent_key, key, node))
        return self

    def build(self) -> TreeHierarchy:
        result = TreeHierarchy()
        for tree_building_block in self._tree_building_blocks:
            result.add_node(
                parent_key=tree_building_block[0],
                node_key=tree_building_block[1],
                node=tree_building_block[2])
        return result
