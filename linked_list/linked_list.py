from typing import Union


class Node:

    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        old_node = self.head
        new_node = Node(value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

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
