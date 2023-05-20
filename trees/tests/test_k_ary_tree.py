from trees.k_ary_tree import KArrTree


def test_k_ary_tree():
    tree = KArrTree[int](4)
    tree.set_root(1)
    tree.root.set_child(0, 2)  # type: ignore
    tree.root.set_child(1, 3)   # type: ignore
    tree.root.get_child(0).set_child(0, 4)  # type: ignore
    tree.root.get_child(0).set_child(1, 5)  # type: ignore
    tree.root.get_child(1).set_child(0, 6)  # type: ignore
    tree.root.get_child(1).set_child(1, 7)  # type: ignore

    assert tree.pre_order_traversal() == [1, 2, 4, 5, 3, 6, 7]
