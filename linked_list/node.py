from typing import Union


class Node:
    """
    A node in a linked list
    """

    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None
