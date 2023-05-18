import pytest
from trees.binary_tree import BinaryTree, Node


def test_binary_tree_empty():
    tree = BinaryTree()
    assert tree.root == None


def test_binary_tree_one_node():
    tree = BinaryTree()
    node = Node('a')
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
    node_a = Node("a")
    node_b = Node("b")
    node_c = Node("c")
    node_a.left = node_b
    node_a.right = node_c

    node_d = Node("d")
    node_e = Node("e")
    node_b.left = node_d
    node_b.right = node_e

    node_f = Node("f")
    node_c.left = node_f

    tree.root = node_a
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
