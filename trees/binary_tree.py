from trees.node import Node
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self._root: Optional[Node[T]] = None

    # region Properties
    @property
    def root(self) -> Optional[Node[T]]: return self._root

    @root.setter
    def root(self, node: Optional[Node[T]]) -> None: self._root = node
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
    # endregion

    # region Static Methods
    @classmethod
    def pre_order_from(cls, node: Optional[Node[T]]) -> list[T]:
        """Returns a list of the values in the tree in pre-order, starting from the given node."""
        if node is None:
            return []
        return ([node.value] + cls.pre_order_from(node.left) + cls.pre_order_from(node.right))

    @classmethod
    def in_order_from(cls, node: Optional[Node[T]]) -> list[T]:
        """Returns a list of the values in the tree in in-order, starting from the given node."""
        if node is None:
            return []
        return (cls.in_order_from(node.left) + [node.value] + cls.in_order_from(node.right))

    @classmethod
    def post_order_from(cls, node: Optional[Node[T]]) -> list[T]:
        """Returns a list of the values in the tree in post-order, starting from the given node."""
        if node is None:
            return []
        return (cls.post_order_from(node.left) + cls.post_order_from(node.right) + [node.value])
    # endregion
