from typing import Generic, Optional, TypeVar

from trees.nodes._k_node import _KNode


T = TypeVar("T")


class KArrTree(Generic[T]):
    def __init__(self, k: int) -> None:
        self._root: Optional[_KNode[T]] = None
        self._k: int = k

    # region property
    @property
    def root(self): return self._root

    @property
    def k(self): return self._k
    # endregion

    def set_root(self, value: T) -> None:
        """Set the root of the tree."""
        if self._root is not None:
            raise ValueError("can't set root, root already exist")
        self._root = _KNode(value, self._k)

    def pre_order_traversal(self) -> list[T]:
        """Pre-order traversal of the tree."""
        return [] if self._root is None else self._pre_order_traversal(self._root)

    @classmethod
    def _pre_order_traversal(cls, node: _KNode[T]) -> list[T]:
        result = [node.value]
        for child in node._children:
            if child is not None:
                result.extend(cls._pre_order_traversal(child))
        return result
