from trees.nodes.binary_node import BinaryNode
from trees.binary_tree import BinaryTree
from typing import TypeVar, Optional, Protocol, Any

# region Typing

T = TypeVar("T", bound='Comparable')


class Comparable(Protocol):
    def __eq__(self, __value: Any) -> bool: ...
    def __ne__(self, __value: Any) -> bool: ...
    def __lt__(self, __value: Any) -> bool: ...
    def __le__(self, __value: Any) -> bool: ...
    def __gt__(self, __value: Any) -> bool: ...
    def __ge__(self, __value: Any) -> bool: ...

# endregion


class BinarySearchTree(BinaryTree[T]):

    @property
    def root(self) -> Optional[BinaryNode[T]]:
        """Returns the root node of the tree.\n
        read-only property, Cannot set root node on binary search tree, use `add` method instead.
        """
        return self._root

    def add(self, value: T) -> None:
        """Adds a value to the tree, maintaining the binary search tree property."""
        if self._root is None:
            self._root = BinaryNode(value, True)
        else:
            self._add(value, self._root)

    def _add(self, value: T, node: BinaryNode[T]) -> None:
        """recursive helper function for add method, adds a value to the tree, maintaining the binary search tree property."""
        if value <= node.value:
            if (node._left is None):
                node._left = BinaryNode(value, True)
                return
            self._add(value, node._left)
        else:
            if (node._right is None):
                node._right = BinaryNode(value, True)
                return
            self._add(value, node._right)

    def contains(self, value: T) -> bool:
        """ Returns True if the value is in the tree, False otherwise."""
        return self._contains(value, self.root)

    def _contains(self, value: T, node: Optional[BinaryNode[T]]) -> bool:
        """recursive helper function for contains method, returns True if the value is in the tree, False otherwise."""
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._contains(value, node.left)
        else:
            return self._contains(value, node.right)
