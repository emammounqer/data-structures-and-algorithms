import pytest
from trees.binary_tree import BinaryTree, BinaryNode


def test_binary_tree_empty():
    tree = BinaryTree()
    assert tree.root is None


def test_binary_tree_one_node():
    tree = BinaryTree()
    node = BinaryNode('a')
    tree.root = node
    assert tree.root == node


@pytest.fixture
def tree():
    #             a
    #     ________|________
    #     b               c
    # ____|____       ____|
    # d       e       f

    tree = BinaryTree()
    tree.root = BinaryNode("a")
    tree.root.left = BinaryNode("b")
    tree.root.right = BinaryNode("c")
    tree.root.left.left = BinaryNode("d")
    tree.root.left.right = BinaryNode("e")
    tree.root.right.left = BinaryNode("f")
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
