
from typing import TypeVar, Generic, Union
from stack_and_queue.node import Node

T = TypeVar("T")


class Queue(Generic[T]):
    """
    Queue implementation using linked list
    """

    def __init__(self):
        self.front: Union[Node[T], None] = None
        self.back: Union[Node[T], None] = None

    def enqueue(self, value: T):
        """dd a new node to the back of the queue"""
        node = Node(value)

        if self.back:
            self.back.next = node
        self.back = node
        if not self.front:
            self.front = node

    def dequeue(self):
        """Remove the node from the front of the queue and return its value"""
        if self.front is None:
            raise IndexError("Empty Queue")

        curr = self.front
        if (self.front == self.back):
            self.back = None
            self.front = None
            return curr.value

        self.front = self.front.next
        return curr.value

    def peek(self):
        """Returns the value of the node located in the front of the queue"""
        if self.front is None:
            raise IndexError("Empty Queue")

        return self.front.value

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        if self.front is None:
            return True
        return False
