from trees.node import Node
from typing import Generic, TypeVar, Optional, Literal

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

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

        left_list = cls.order(node.left, method)
        right_list = cls.order(node.right, method)

        if method == 'pre':
            return ([node.value] + left_list + right_list)
        elif method == 'in':
            return (left_list + [node.value] + right_list)
        elif method == 'post':
            return (left_list + right_list + [node.value])
