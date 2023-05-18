from trees.node import Node
from typing import Generic, TypeVar, Optional, Literal

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

    def pre_order(self) -> list[T]:
        return self.order(self.root, 'pre')

    def in_order(self) -> list[T]:
        return self.order(self.root, 'in')

    def post_order(self) -> list[T]:
        return self.order(self.root, 'post')

    @classmethod
    def order(cls, node: Optional[Node[T]], method: Literal['pre', 'in', 'post']) -> list[T]:
        if node is None:
            return []
        elif method == 'pre':
            return ([node.value] + cls.order(node.left, method) + cls.order(node.right, method))
        elif method == 'in':
            return (cls.order(node.left, method) + [node.value] + cls.order(node.right, method))
        elif method == 'post':
            return (cls.order(node.left, method) + cls.order(node.right, method) + [node.value])
