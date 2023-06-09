import pytest
from linked_list.linked_list_adv import LinkedList


@pytest.fixture
def linked_list():
    linked_list = LinkedList[int]()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    return linked_list


def test_linked_list():
    actual = LinkedList()
    expected = None
    assert actual.head == expected


def test_linked_list_insert():
    actual = LinkedList()
    actual.insert(1)
    excepted = 1
    assert actual.head is not None
    assert actual.head.value == excepted


def test_linked_list_insert_multiple():
    actual = LinkedList()
    actual.insert(1)
    actual.insert(2)
    actual.insert(3)
    assert actual[0] == 3
    assert actual[1] == 2
    assert actual[2] == 1


def test_linked_list_index_error(linked_list: LinkedList):
    with pytest.raises(IndexError):
        linked_list[5]


def test_linked_list_length(linked_list: LinkedList):
    actual = len(linked_list)
    expected = 3
    assert actual == expected


def test_linked_list_head(linked_list: LinkedList):
    head = linked_list.head
    assert head is not None
    assert head.value == 3


def test_linked_list_includes(linked_list: LinkedList):
    actual = linked_list.includes(1)
    expected = True
    assert actual == expected


def test_linked_list_includes_false(linked_list: LinkedList):
    actual = linked_list.includes(4)
    expected = False
    assert actual == expected


def test_linked_list_to_string(linked_list: LinkedList):
    actual = linked_list.to_string()
    expected = "{ 3 } -> { 2 } -> { 1 } -> NONE"
    assert actual == expected


def test_insert_before_in_middle(linked_list: LinkedList):
    linked_list.insert_before(2, 7)
    assert linked_list[1] == 7


def test_insert_before_at_head(linked_list: LinkedList):
    linked_list.insert_before(3, 7)
    assert linked_list[0] == 7


def test_insert_before_at_end(linked_list: LinkedList):
    linked_list.insert_before(1, 7)
    assert linked_list[2] == 7


def test_insert_before_at_not_exist(linked_list: LinkedList):
    with pytest.raises(ValueError):
        linked_list.insert_before(11, 7)


def test_insert_after_in_middle(linked_list: LinkedList):
    linked_list.insert_after(2, 7)
    assert linked_list[2] == 7


def test_insert_after_at_head(linked_list: LinkedList):
    linked_list.insert_after(3, 7)
    assert linked_list[1] == 7


def test_insert_after_at_end(linked_list: LinkedList):
    linked_list.insert_after(1, 7)
    assert linked_list[3] == 7


def test_insert_after_at_not_exist(linked_list: LinkedList):
    with pytest.raises(ValueError):
        linked_list.insert_after(11, 7)

# Input ll	Arg k	Output
# head -> {1} -> {3} -> {8} -> {2} -> X	0	2
# head -> {1} -> {3} -> {8} -> {2} -> X	2	3
# head -> {1} -> {3} -> {8} -> {2} -> X	6	Exception


@pytest.fixture
def linked_list_two():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    return linked_list


@pytest.mark.parametrize('kth,expected', [(0, 2), (2, 3)])
def test_kth_from_end_h(linked_list_two: LinkedList, kth, expected):
    print(linked_list_two)
    actual = linked_list_two.kth_from_end(kth)
    assert actual == expected


def test_kth_from_end_out_of_rage(linked_list_two: LinkedList):
    with pytest.raises(IndexError):
        linked_list_two.kth_from_end(6)
