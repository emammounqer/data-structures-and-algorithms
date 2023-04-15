from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Union[Node[T], None] = None


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self.head:  Union[Node[T], None] = None
        self.length = 0

    def __iter__(self):
        curr = self.head
        while (curr is not None):
            yield curr
            curr = curr.next

    def __getitem__(self, index: int):
        if index < 0:
            raise IndexError("Index must be positive")

        for i, node in enumerate(self):
            if i == index:
                return node
        raise IndexError("Index out of range")

    def insert(self, value: T):
        old_node = self.head
        new_node = Node[T](value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

    def includes(self, value: T) -> bool:
        for node in self:
            if node.value == value:
                return True
        return False

    def to_string(self):
        output = ""
        for node in self:
            output += f"{{ {node.value} }} -> "
        output += "NONE"
        return output
