from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class BinaryNode(Generic[T]):
    def __init__(self, value: T, protected=False) -> None:
        """
        Creates a new node with the given value.
        args:
            value: the value to be stored in the node.
            protected: if True, the node cannot be modified after creation outside the tree.
        """
        self._value = value
        self._left: Optional[BinaryNode[T]] = None
        self._right: Optional[BinaryNode[T]] = None
        self._protected = protected

    # region Properties
    @property
    def value(self) -> T: return self._value

    @value.setter
    def value(self, value: T) -> None:
        if self.protected:
            raise ValueError(
                'Cannot set value on protected node, use `add` method in the tree instead.')
        self._value = value

    @property
    def left(self) -> Optional['BinaryNode[T]']: return self._left

    @left.setter
    def left(self, node: Optional['BinaryNode[T]']) -> None:
        if self.protected:
            raise ValueError(
                'Cannot set left node on protected node, use `add` method in the tree instead.')
        self._left = node

    @property
    def right(self) -> Optional['BinaryNode[T]']: return self._right

    @right.setter
    def right(self, node: Optional['BinaryNode[T]']) -> None:
        if self.protected:
            raise ValueError(
                'Cannot set right node on protected node, use `add` method in the tree instead.')
        self._right = node

    @property
    def protected(self) -> bool: return self._protected
    # endregion
