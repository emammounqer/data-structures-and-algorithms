from typing import Optional, TypeVar
from trees.INode import INode

T = TypeVar("T", int, str, float, bytes, bytearray)


class NodeBinarySearch(INode[T]):
    def __init__(self, value: T) -> None:
        self._value: T = value
        self._left: Optional[NodeBinarySearch[T]] = None
        self._right: Optional[NodeBinarySearch[T]] = None

    @property
    def value(self) -> T:
        """Returns the value of the node."""
        return self._value

    @property
    def left(self) -> Optional['NodeBinarySearch[T]']:
        """Returns the left child of the node."""
        return self._left

    @left.setter
    def left(self, node: 'NodeBinarySearch[T]') -> None:
        """Sets the left child of the node."""
        if node.value > self._value:
            raise ValueError(
                'Cannot set left child be bigger than curr value of node in binary search tree.')
        if not isinstance(node, NodeBinarySearch):
            raise TypeError("node must be of type NodeBinarySearch.")
        self._left = node

    @property
    def right(self) -> Optional['NodeBinarySearch[T]']:
        """Returns the right child of the node."""
        return self._right

    @right.setter
    def right(self, node: 'NodeBinarySearch[T]') -> None:
        """Sets the right child of the node."""
        if node._value < self._value:
            raise ValueError(
                "Cannot set right child be smaller than curr value of node in binary search tree.")
        if not isinstance(node, NodeBinarySearch):
            raise TypeError("node must be of type NodeBinarySearch.")
        self._right = node
