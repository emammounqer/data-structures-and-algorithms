from trees.node import Node
from trees.binary_tree import BinaryTree
from typing import TypeVar, Optional


T = TypeVar("T", int, str, float, bytes, bytearray)


class BinarySearchTree(BinaryTree[T]):
    """A binary search tree implementation."""

    @property
    def root(self) -> Optional[Node[T]]:
        return self._root

    @root.setter
    def root(self, node: Optional[Node[T]]):
        """you can't set the root of a binary search tree Use the add method instead"""
        raise AttributeError(
            "you can't set the root of a binary search tree Use the `add` method instead")

    def add(self, value: T) -> None:
        """Adds a value to the tree, maintaining the binary search tree property."""
        if self.root is None:
            self._root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value: T, node: Node[T]) -> None:
        """recursive helper function for add method, adds a value to the tree, maintaining the binary search tree property."""
        if value <= node.value:
            if (node.left is None):
                node.left = Node(value)
                return
            self._add(value, node.left)
        else:
            if (node.right is None):
                node.right = Node(value)
                return
            self._add(value, node.right)

    def contains(self, value: T) -> bool:
        """ Returns True if the value is in the tree, False otherwise."""
        return self._contains(value, self.root)

    def _contains(self, value: T, node: Optional[Node[T]]) -> bool:
        """recursive helper function for contains method, returns True if the value is in the tree, False otherwise."""
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._contains(value, node.left)
        else:
            return self._contains(value, node.right)
