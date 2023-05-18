import pytest
from trees.node import Node
from trees.binary_search_tree import BinarySearchTree


@pytest.fixture
def tree():
    #             50
    #     ________|________
    #     21              76
    # ____|____       ____|
    # 7       40      65

    tree = BinarySearchTree[int]()
    tree.add(50)
    tree.add(21)
    tree.add(76)
    tree.add(7)
    tree.add(40)
    tree.add(65)

    return tree


def test_binary_search_tree_add_one():
    tree = BinarySearchTree()
    tree.add(50)
    assert tree.root and tree.root.value == 50


def test_binary_search_tree_add_two():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(21)
    assert tree.root and tree.root.value == 50
    assert tree.root.left and tree.root.left.value == 21


def test_binary_search_tree_add_many(tree: BinarySearchTree):
    assert tree.root and tree.root.value == 50
    assert tree.root.left and tree.root.left.value == 21
    assert tree.root.right and tree.root.right.value == 76
    assert tree.root.left.left and tree.root.left.left.value == 7
    assert tree.root.left.right and tree.root.left.right.value == 40
    assert tree.root.right.left and tree.root.right.left.value == 65


def test_binary_search_tree_contains_true(tree: BinarySearchTree):
    assert tree.contains(50) == True
    assert tree.contains(21) == True
    assert tree.contains(76) == True
    assert tree.contains(7) == True
    assert tree.contains(40) == True
    assert tree.contains(65) == True


def test_binary_search_tree_contains_false(tree: BinarySearchTree):
    assert tree.contains(51) == False
    assert tree.contains(22) == False
    assert tree.contains(75) == False
    assert tree.contains(8) == False
    assert tree.contains(39) == False
    assert tree.contains(66) == False
