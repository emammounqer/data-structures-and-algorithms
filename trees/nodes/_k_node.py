from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class _KNode(Generic[T]):
    def __init__(self, value: T, k: int) -> None:
        self.value: T = value
        self._children: list[Optional['_KNode']] = [None] * k

    def get_child(self, index: int) -> Optional['_KNode']:
        return self._children[index]

    def set_child(self, index: int, value: T) -> None:
        self._children[index] = _KNode(value, len(self._children))
