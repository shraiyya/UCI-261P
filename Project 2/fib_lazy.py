# explanations for member functions are provided in requirements.py

# 12041645
# Shreya Chetan Pawaskar
# pawaskas@uci.edu

from __future__ import annotations

class FibNodeLazy:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNodeLazy):
        return self.val == other.val

class FibHeapLazy:
    def __init__(self):
        self.roots = []
        #self.min = None

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNodeLazy:
        new_node = FibNodeLazy(val)
        self.roots.append(new_node)
        return new_node
        
    def delete_min_lazy(self) -> None:
        if not self.roots:
            return

        min_node = min(self.roots, key=lambda x: x.val)
        self.roots.remove(min_node)

        if min_node.children:
            for child in min_node.children:
                self.roots.append(child)
                child.parent = None

    def find_min_lazy(self) -> FibNodeLazy:
        if not self.roots:
            return None
        return min(self.roots, key=lambda x: x.val)

    def decrease_priority(self, node: FibNodeLazy, new_val: int) -> None:
        if new_val > node.val:
            raise ValueError("Error")

        node.val = new_val
        parent = node.parent

        if parent and node.val < parent.val:
            self.promote(node, parent)
            self.cascade(parent)

    def promote(self, node: FibNodeLazy, parent: FibNodeLazy) -> None:
        # Promote a node to the root list
        if node in parent.children:
            parent.children.remove(node)
            self.roots.append(node)
            node.parent = None
            node.flag = False

    def cascade(self, node: FibNodeLazy) -> None:
        # Cascade cut operation to promote nodes recursively
        parent = node.parent
        if parent:
            if not node.flag:
                node.flag = True
            else:
                self.promote(node, parent)
                self.cascade(parent)

    def traverse_and_destroy_vacant_nodes(self, node: FibNodeLazy, new_roots: list) -> None:
        # Traverse the tree and destroy vacant nodes
        if node.get_flag():
            # Destroy vacant nodes
            self.destroy_vacant_nodes(node)
            return
        new_roots.append(node)
        for child in node.children:
            self.traverse_and_destroy_vacant_nodes(child, new_roots)

    def destroy_vacant_nodes(self, node: FibNodeLazy) -> None:
        # Destroy vacant nodes in the tree
        node.flag = False
        new_children = []
        for child in node.children:
            if not child.get_flag():
                new_children.append(child)
            else:
                self.destroy_vacant_nodes(child)
        node.children = new_children
