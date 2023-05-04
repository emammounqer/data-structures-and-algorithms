from typing import Generic, TypeVar, Union
from stack_and_queue.node import Node

T = TypeVar("T")


class Stack(Generic[T]):

    def __init__(self) -> None:
        self.top: Union[Node[T], None] = None

    def push(self, value: T) -> None:
        """
        Push a new node onto the stack

        Args:
            value (any): The value of the new node
        """
        old_top = self.top
        self.top = Node(value)
        self.top.next = old_top

    def pop(self):
        """
        Pop the top node off the stack

        Returns:
            any: The value of the top node
        """
        if self.top is None:
            raise IndexError("Cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Peek at the top node of the stack

        Returns:
            any: The value of the top node
        """
        if self.top is None:
            raise IndexError("Cannot peek at an empty stack")
        return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty

        Returns:
            bool: True if the stack is empty, False otherwise
        """
        if self.top is None:
            return True
        return False
