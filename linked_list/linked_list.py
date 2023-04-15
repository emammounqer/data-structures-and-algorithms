from typing import Union


class Node:

    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        return self.to_string()

    def insert(self, value):
        old_node = self.head
        new_node = Node(value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

    def insert_multiple(self, *values):
        for value in values:
            self.insert(value)

    def append(self, value):
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

    def delete(self, value):
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

    def includes(self, value):
        curr = self.head
        while (curr is not None):
            if (curr.value == value):
                return True
            curr = curr.next
        return False

    def to_string(self):
        output = ""
        curr = self.head
        while (curr is not None):
            output += f"{{ {curr.value} }} -> "
            curr = curr.next
        output += "NONE"
        return output
