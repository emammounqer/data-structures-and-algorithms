from typing import Generic, TypeVar, Union

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.left: Union[Node[T], None] = None
        self.right: Union[Node[T], None] = None
