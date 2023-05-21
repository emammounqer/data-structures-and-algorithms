from trees.nodes.binary_node import BinaryNode
from typing import Generator, Generic, Iterable, TypeVar, Optional

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self._root: Optional[BinaryNode[T]] = None

    # region Properties

    @property
    def root(self) -> Optional[BinaryNode[T]]: return self._root

    @root.setter
    def root(self, node: Optional[BinaryNode[T]]) -> None:
        if isinstance(node, BinaryNode):
            self._root = node
        else:
            raise TypeError("root must be of type BinaryNode")
    # endregion

    # region Magic Methods
    def __iter__(self):
        if self._root is None:
            return
        yield from self.__iter_from(self._root)

    def __iter_from(self, node: BinaryNode[T]) -> Generator[T, None, None]:
        yield node.value
        if node.left is not None:
            yield from self.__iter_from(node.left)
        if node.right is not None:
            yield from self.__iter_from(node.right)
    # endregion

    # region Methods

    def pre_order(self) -> list[T]:
        """Returns a list of the values in the tree in pre-order."""
        return self.pre_order_from(self._root)

    def in_order(self) -> list[T]:
        """Returns a list of the values in the tree in in-order."""
        return self.in_order_from(self._root)

    def post_order(self) -> list[T]:
        """Returns a list of the values in the tree in post-order."""
        return self.post_order_from(self._root)

    def max_value(self) -> T:
        """Returns the maximum value in the tree."""
        if self._root is None:
            raise ValueError("Tree is empty")
        max_value = self._root.value
        for v in self:
            if v > max_value:  # type: ignore
                max_value = v
        return max_value

    # endregion

    # region Static Methods
    @classmethod
    def pre_order_from(cls, node: Optional[BinaryNode[T]]) -> list[T]:
        """Returns a list of the values in the tree in pre-order, starting from the given node."""
        if node is None:
            return []
        return ([node.value] + cls.pre_order_from(node.left) + cls.pre_order_from(node.right))

    @classmethod
    def in_order_from(cls, node: Optional[BinaryNode[T]]) -> list[T]:
        """Returns a list of the values in the tree in in-order, starting from the given node."""
        if node is None:
            return []
        return (cls.in_order_from(node.left) + [node.value] + cls.in_order_from(node.right))

    @classmethod
    def post_order_from(cls, node: Optional[BinaryNode[T]]) -> list[T]:
        """Returns a list of the values in the tree in post-order, starting from the given node."""
        if node is None:
            return []
        return (cls.post_order_from(node.left) + cls.post_order_from(node.right) + [node.value])
    # endregion
