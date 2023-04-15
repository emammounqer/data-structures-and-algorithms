from typing import Union, TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.next: Union[Node[T], None] = None
        self.prev: Union[Node[T], None] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Union[Node[T], None] = None
        self.tail: Union[Node[T], None] = None
        self.length = 0

    def __str__(self):
        output = ""
        curr = self.head
        while (curr is not None):
            output += f"{{ {curr.value} }} -> "
            curr = curr.next
        output += "NONE"
        return output

    def insert(self, value: T):
        new_node = Node[T](value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, value: T):
        new_node = Node[T](value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def includes(self, value: T):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
