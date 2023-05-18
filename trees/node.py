from typing import TypeVar, Optional

from trees.INode import INode

T = TypeVar('T')


class Node(INode[T]):
    def __init__(self, value: T) -> None:
        self._value = value
        self._left: Optional[Node[T]] = None
        self._right: Optional[Node[T]] = None

    @property
    def value(self) -> T:
        """Returns the value of the node."""
        return self._value

    @property
    def left(self) -> Optional['Node[T]']:
        """Returns the left child of the node."""
        return self._left

    @left.setter
    def left(self, node: 'Node[T]') -> None:
        """Sets the left child of the node."""
        self._left = node

    @property
    def right(self) -> Optional['Node[T]']:
        """Returns the right child of the node."""
        return self._right

    @right.setter
    def right(self, node: 'Node[T]') -> None:
        """Sets the right child of the node."""
        self._right = node
