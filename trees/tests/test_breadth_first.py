from trees.breadth_first import breadth_first, BinaryTree, BinaryNode


def test_breadth_first_happy_path():
    #        2
    #      /  \
    #     7     5
    #    / \     \
    #   2   6     9
    #      / \    /
    #     5  11  4

    tree = BinaryTree()
    node_2 = BinaryNode(2)
    node_7 = BinaryNode(7)
    node_5 = BinaryNode(5)
    node_2_7 = BinaryNode(2)
    node_6 = BinaryNode(6)
    node_9 = BinaryNode(9)
    node_5_6 = BinaryNode(5)
    node_11 = BinaryNode(11)
    node_4 = BinaryNode(4)

    node_2.left = node_7
    node_2.right = node_5
    node_7.left = node_2_7
    node_7.right = node_6
    node_5.right = node_9
    node_6.left = node_5_6
    node_6.right = node_11
    node_9.left = node_4

    tree.root = node_2
    actual = breadth_first(tree)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]

    assert actual == expected


def test_breadth_first_one_node():
    tree = BinaryTree()
    tree.root = BinaryNode(2)
    actual = breadth_first(tree)
    assert actual == [2]


def test_breadth_first_empty_tree():
    tree = BinaryTree()
    actual = breadth_first(tree)
    assert actual == []
