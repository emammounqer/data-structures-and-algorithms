from tree_intersection.tree_intersection import tree_intersection
from trees.binary_tree import BinaryTree, BinaryNode


def test_tree_intersection():
    tree1 = BinaryTree()
    tree1.root = BinaryNode(150)
    tree1.root.left = BinaryNode(100)
    tree1.root.left.left = BinaryNode(75)
    tree1.root.left.right = BinaryNode(160)
    tree1.root.left.right.left = BinaryNode(125)
    tree1.root.left.right.right = BinaryNode(175)
    tree1.root.right = BinaryNode(250)
    tree1.root.right.left = BinaryNode(200)
    tree1.root.right.right = BinaryNode(350)
    tree1.root.right.right.left = BinaryNode(300)
    tree1.root.right.right.right = BinaryNode(500)

    tree2 = BinaryTree()
    tree2.root = BinaryNode(42)
    tree2.root.left = BinaryNode(100)
    tree2.root.left.left = BinaryNode(15)
    tree2.root.left.right = BinaryNode(160)
    tree2.root.left.right.left = BinaryNode(125)
    tree2.root.left.right.right = BinaryNode(175)
    tree2.root.right = BinaryNode(600)
    tree2.root.right.left = BinaryNode(200)
    tree2.root.right.right = BinaryNode(350)
    tree2.root.right.right.left = BinaryNode(4)
    tree2.root.right.right.right = BinaryNode(500)

    actual = tree_intersection(tree1, tree2)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual == expected


def test_tree_intersection_empty_tree():
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected


def test_tree_intersection_one_empty_tree():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree2.root = BinaryNode(42)
    tree2.root.left = BinaryNode(100)
    tree2.root.left.left = BinaryNode(15)
    tree2.root.left.right = BinaryNode(160)
    tree2.root.left.right.left = BinaryNode(125)
    tree2.root.left.right.right = BinaryNode(175)
    tree2.root.right = BinaryNode(600)
    tree2.root.right.left = BinaryNode(200)
    tree2.root.right.right = BinaryNode(350)
    tree2.root.right.right.left = BinaryNode(4)
    tree2.root.right.right.right = BinaryNode(500)

    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected


def test_tree_intersection_one_node_tree():
    tree1 = BinaryTree()
    tree1.root = BinaryNode(150)
    tree2 = BinaryTree()
    tree2.root = BinaryNode(150)

    actual = tree_intersection(tree1, tree2)
    expected = [150]
    assert actual == expected


def test_tree_intersection_no_intersection():
    tree1 = BinaryTree()
    tree1.root = BinaryNode(150)
    tree1.root.left = BinaryNode(100)
    tree1.root.left.left = BinaryNode(75)
    tree1.root.left.right = BinaryNode(160)
    tree1.root.left.right.left = BinaryNode(125)
    tree1.root.left.right.right = BinaryNode(175)
    tree1.root.right = BinaryNode(250)
    tree1.root.right.left = BinaryNode(200)
    tree1.root.right.right = BinaryNode(350)
    tree1.root.right.right.left = BinaryNode(300)
    tree1.root.right.right.right = BinaryNode(500)

    tree2 = BinaryTree()
    tree2.root = BinaryNode(42)
    tree2.root.left = BinaryNode(101)
    tree2.root.left.left = BinaryNode(15)
    tree2.root.left.right = BinaryNode(16)
    tree2.root.left.right.left = BinaryNode(126)
    tree2.root.left.right.right = BinaryNode(176)
    tree2.root.right = BinaryNode(600)
    tree2.root.right.left = BinaryNode(201)
    tree2.root.right.right = BinaryNode(351)
    tree2.root.right.right.left = BinaryNode(4)
    tree2.root.right.right.right = BinaryNode(501)

    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected
