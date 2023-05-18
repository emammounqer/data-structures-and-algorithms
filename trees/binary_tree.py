from trees.node import Node
from typing import Generic, TypeVar, Optional, Literal

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self._root: Optional[Node[T]] = None

    @property
    def root(self) -> Optional[Node[T]]:
        return self._root

    @root.setter
    def root(self, value: Optional[Node[T]]):
        self._root = value

    def pre_order(self) -> list[T]:
        """Returns a list of the values in the tree in pre-order."""
        return self.order(self.root, 'pre')

    def in_order(self) -> list[T]:
        """Returns a list of the values in the tree in in-order."""
        return self.order(self.root, 'in')

    def post_order(self) -> list[T]:
        """Returns a list of the values in the tree in post-order."""
        return self.order(self.root, 'post')

    @classmethod
    def order(cls, node: Optional[Node[T]], method: Literal['pre', 'in', 'post']) -> list[T]:
        """Returns a list of the values in the tree in the specified order.

        The three possible orders are:
        - pre: root, left, right
        - in: left, root, right
        - post: left, right, root
        """
        if node is None:
            return []
        elif method == 'pre':
            return ([node.value] + cls.order(node.left, method) + cls.order(node.right, method))
        elif method == 'in':
            return (cls.order(node.left, method) + [node.value] + cls.order(node.right, method))
        elif method == 'post':
            return (cls.order(node.left, method) + cls.order(node.right, method) + [node.value])
