from trees.INode import INode
from trees.node import Node
from typing import Generic, TypeVar, Optional, Literal

VT = TypeVar("VT")


class BinaryTree(Generic[VT]):
    def __init__(self):
        self._root: Optional[INode[VT]] = None

    @property
    def root(self) -> Optional[INode[VT]]:
        """Returns the root of the tree."""
        return self._root

    @root.setter
    def root(self, node: INode[VT]) -> None:
        """Sets the root of the tree."""
        self._root = node

    def pre_order(self) -> list[VT]:
        """Returns a list of the values in the tree in pre-order."""
        return self.order(self._root, 'pre')

    def in_order(self) -> list[VT]:
        """Returns a list of the values in the tree in in-order."""
        return self.order(self._root, 'in')

    def post_order(self) -> list[VT]:
        """Returns a list of the values in the tree in post-order."""
        return self.order(self._root, 'post')

    @classmethod
    def order(cls, node: Optional[INode[VT]], method: Literal['pre', 'in', 'post']) -> list[VT]:
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
