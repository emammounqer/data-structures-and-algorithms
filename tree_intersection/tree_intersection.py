from trees.binary_tree import BinaryTree, BinaryNode
from hashtable.hashtable import Hashtable


def tree_intersection(tree1: BinaryTree, tree2: BinaryTree):
    """
    Function that takes two binary tree parameters and returns a list of the values found in both trees.
    """
    hashtable = Hashtable()

    values = []
    for value in tree1:
        hashtable.set(value, 1)

    for value in tree2:
        if hashtable.has(value):
            values.append(value)

    return values
