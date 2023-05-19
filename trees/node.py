from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, protected=False) -> None:
        """
        Creates a new node with the given value.
        args:
            value: the value to be stored in the node.
            protected: if True, the node cannot be modified after creation.
        """
        self._value = value
        self._left: Optional[Node[T]] = None
        self._right: Optional[Node[T]] = None
        self._protected = protected

    @property
    def value(self) -> T: return self._value

    @property
    def left(self) -> Optional['Node[T]']: return self._left

    @left.setter
    def left(self, node: Optional['Node[T]']) -> None:
        if self.protected:
            raise AttributeError(
                'Cannot set left node on protected node, use `add` method in the tree instead.')
        self._left = node

    @property
    def right(self) -> Optional['Node[T]']: return self._right

    @right.setter
    def right(self, node: Optional['Node[T]']) -> None:
        if self.protected:
            raise AttributeError(
                'Cannot set right node on protected node, use `add` method in the tree instead.')
        self._right = node

    @property
    def protected(self) -> bool: return self._protected
