import pytest
from trees.binary_tree import BinaryTree, Node


@pytest.fixture
def tree():
    #             a
    #     ________|________
    #     b               c
    # ____|____       ____|
    # d       e       f

    tree = BinaryTree()
    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    return tree


def test_binary_tree_pre_order(tree: BinaryTree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f"]
    assert actual == expected


def test_binary_tree_in_order(tree: BinaryTree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c"]
    assert actual == expected


def test_binary_tree_post_order(tree: BinaryTree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "c", "a"]
    assert actual == expected
