from trees.binary_tree import BinaryTree, BinaryNode
from stack_and_queue.queue import Queue
from typing import TypeVar

T = TypeVar("T")


def breadth_first(tree: BinaryTree[T]) -> list[T]:
    queue = Queue[BinaryNode[T]]()
    result: list[T] = []

    if tree.root is not None:
        queue.enqueue(tree.root)

    while not queue.is_empty():
        curr = queue.dequeue()
        result.append(curr.value)
        if curr.left is not None:
            queue.enqueue(curr.left)
        if curr.right is not None:
            queue.enqueue(curr.right)

    return result
