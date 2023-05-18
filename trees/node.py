from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None
