import copy
from abc import ABC
from typing import Any, Optional, List, Iterator


class TreeNodeContainer:
    def __init__(self, key: Any, node: Any):
        self.children = []  # type: List[TreeNodeContainer]
        self.key = key  # type: Any
        self.node = node  # type: Any


class TreeNodeIter:
    def __init__(self, parent: Optional[Any], node: Any, parent_key: Optional[Any], key: Any, children: List[TreeNodeContainer]):
        self.parent = parent  # type: Optional[Any]
        self.node = node  # type: Any
        self.parent_key = parent_key  # type: Optional[Any]
        self.key = key  # type: Any
        self.children = children  # type: List[TreeNodeContainer]


class TreeNodeInfo:
    def __init__(self, parent_key: Optional[Any], node: Any):
        self.parent_key = parent_key  # Optional[Any]
        self.node = node  # type: Any


class TreeHierarchy(ABC):
    def __init__(self):
        self.roots = []  # type: List[TreeNodeContainer]

    def _traverse_children_recursively_and_put(
            self, parent_key: Any, node_to_put: TreeNodeContainer):
        for node_iter in self.iterate_nodes():
            if node_iter.key == parent_key:
                node_iter.children.append(node_to_put)
                return
        raise Exception(
            "Did not find parent of that key in tree hierarchy to put node in it: {}".format(parent_key))

    def _traverse_nodes_hierarchy(self, parent: Optional[TreeNodeContainer],
                                  current_node: TreeNodeContainer) -> Iterator[TreeNodeIter]:
        for child_node in current_node.children:
            yield TreeNodeIter(parent=current_node.node,
                               node=child_node.node,
                               parent_key=current_node.key,
                               key=child_node.key,
                               children=child_node.children)
        for child_node in current_node.children:
            yield from self._traverse_nodes_hierarchy(parent=current_node, current_node=child_node)

    def add_node(self, parent_key: Optional[Any], node_key: Any, node: Any):
        node = copy.deepcopy(node)
        node_container = TreeNodeContainer(node=node, key=node_key)
        if parent_key is None:
            self.roots.append(node_container)
        else:
            self._traverse_children_recursively_and_put(
                parent_key=parent_key,
                node_to_put=node_container)

    def iterate_nodes(self) -> Iterator[TreeNodeIter]:
        for root in self.roots:
            yield TreeNodeIter(parent=None,
                               node=root.node,
                               parent_key=None,
                               key=root.key,
                               children=root.children)

        for root in self.roots:                       
            yield from self._traverse_nodes_hierarchy(parent=None, current_node=root)

    def iterate_parent_child_key_pairs(self):
        for node_iter in self.iterate_nodes():
            yield (node_iter.parent_key, node_iter.key)

    def get_node(self, key: Any) -> TreeNodeInfo:
        for node_iter in self.iterate_nodes():
            if node_iter.key == key:
                node = copy.deepcopy(node_iter.node)
                return TreeNodeInfo(parent_key=node_iter.parent_key if node_iter.parent is not None else None,
                                    node=node)
        raise Exception("Did not find node of that key in tree hierarchy: {}".format(key))

    # def get_root(self) -> TreeNodeContainer:
    #    return self.root

    def extend_tree_hierarchy(self, new_nodes_infos):
        while len(new_nodes_infos) > 0:
            new_node_info = new_nodes_infos.pop()
            parent_key = new_node_info[0]

            if parent_key is None or parent_key in [node.key for node in self.iterate_nodes()]:
                node_key = new_node_info[1]
                new_node = new_node_info[2]
                self.add_node(
                    parent_key=parent_key,
                    node_key=node_key,
                    node=new_node
                )
            else:
                new_nodes_infos.add(new_node_info)

    def parent_current_roots_to_new_root(self, node_key: Any, node: Any):
        roots_list = self.roots  # type: List[TreeNodeContainer]
        self.roots = []

        new_root_node_container = TreeNodeContainer(key=node_key, node=node)
        new_root_node_container.children = roots_list

        self.roots.append(new_root_node_container)
