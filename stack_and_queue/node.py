from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Union[Node[T], None] = None
