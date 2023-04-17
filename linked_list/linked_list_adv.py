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

    def __str__(self):
        return self.to_string()

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
                return node.value
        raise IndexError("Index out of range")

    def __len__(self):
        return self.length

    def insert(self, value: T):
        old_node = self.head
        new_node = Node[T](value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

    def insert_before(self, value: T, new_value: T):
        new_node = Node(new_value)
        prev = None
        for node in self:
            if node.value == value:
                if prev is not None:
                    prev.next = new_node
                else:
                    self.head = new_node
                new_node.next = node
                return

            prev = node

        raise ValueError("Value not found")

    def insert_after(self, value: T, new_value: T):
        new_node = Node(new_value)
        for node in self:
            if node.value == value:
                new_node.next = node.next
                node.next = new_node
                return

        raise ValueError("Value not found")

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

    def insert_multiple(self, *values: T):
        for value in values:
            self.insert(value)

    def append(self, value: T):
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.length += 1
            return

        curr = self.head
        while (curr.next is not None):
            curr = curr.next
        curr.next = new_node
        self.length += 1

    def delete(self, value: T):
        curr = self.head
        prev = None

        while (curr is not None):
            if (curr.value == value):
                if (prev is None):
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self.length -= 1
                return
            prev = curr
            curr = curr.next
