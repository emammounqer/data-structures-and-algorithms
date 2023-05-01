import pytest
from linked_list.linked_list import LinkedList


@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.append(1)
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


def test_linked_list_insert_multiple(linked_list: LinkedList):
    actual = str(linked_list)
    expected = "{ 3 } -> { 2 } -> { 1 } -> NONE"
    assert actual == expected


def test_linked_list_length(linked_list: LinkedList):
    actual = linked_list.length
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


def test_linked_list_to_string_None():
    actual = LinkedList().to_string()
    expected = "NONE"
    assert actual == expected


def test_linked_list_to_string(linked_list: LinkedList):
    actual = linked_list.to_string()
    expected = "{ 3 } -> { 2 } -> { 1 } -> NONE"
    assert actual == expected


def test_linked_list_append_one():
    actual = LinkedList()
    actual.append(1)
    expected = 1
    assert actual.head is not None
    assert actual.head.value == expected


def test_linked_list_append_multiple():
    actual = LinkedList()
    actual.append(1)
    actual.append(2)
    actual.append(3)
    expected = "{ 1 } -> { 2 } -> { 3 } -> NONE"
    assert actual.to_string() == expected


def test_linked_list_delete():
    actual = LinkedList()
    actual.insert(1)
    actual.insert(2)
    actual.insert(3)
    actual.delete(2)
    expected = "{ 3 } -> { 1 } -> NONE"
    assert actual.to_string() == expected


def test_linked_list_delete_not_found():
    actual = LinkedList()
    actual.insert(1)
    actual.insert(2)
    actual.insert(3)
    actual.delete(5)
    expected = "{ 3 } -> { 2 } -> { 1 } -> NONE"
    assert actual.to_string() == expected


def test_insert_before_in_middle(linked_list: LinkedList):
    linked_list.insert_before(2, 7)
    expected = "{ 3 } -> { 7 } -> { 2 } -> { 1 } -> NONE"
    assert str(linked_list) == expected


def test_insert_before_at_head(linked_list: LinkedList):
    linked_list.insert_before(3, 7)
    expected = "{ 7 } -> { 3 } -> { 2 } -> { 1 } -> NONE"
    assert str(linked_list) == expected


def test_insert_before_at_end(linked_list: LinkedList):
    linked_list.insert_before(1, 7)
    expected = "{ 3 } -> { 2 } -> { 7 } -> { 1 } -> NONE"
    assert str(linked_list) == expected


def test_insert_before_at_not_exist(linked_list: LinkedList):
    with pytest.raises(ValueError):
        linked_list.insert_before(11, 7)


def test_insert_after_in_middle(linked_list: LinkedList):
    linked_list.insert_after(2, 7)
    expected = "{ 3 } -> { 2 } -> { 7 } -> { 1 } -> NONE"
    assert str(linked_list) == expected


def test_insert_after_at_head(linked_list: LinkedList):
    linked_list.insert_after(3, 7)
    expected = "{ 3 } -> { 7 } -> { 2 } -> { 1 } -> NONE"
    assert str(linked_list) == expected


def test_insert_after_at_end(linked_list: LinkedList):
    linked_list.insert_after(1, 7)
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 7 } -> NONE"
    assert str(linked_list) == expected


def test_insert_after_at_not_exist(linked_list: LinkedList):
    with pytest.raises(ValueError):
        linked_list.insert_after(11, 7)


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


def test_zip_lists():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_one.append(2)
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)
    linked_list_two.append(4)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NONE"
    assert str(actual) == expected


def test_zip_lists_one_longer():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_one.append(2)
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NONE"
    assert str(actual) == expected


def test_zip_lists_two_longer():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)
    linked_list_two.append(4)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NONE"

    assert str(actual) == expected


def test_zip_lists_one_empty():
    linked_list_one = LinkedList()
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)
    linked_list_two.append(4)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 5 } -> { 9 } -> { 4 } -> NONE"
    assert str(actual) == expected


def test_zip_lists_two_empty():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_one.append(2)
    linked_list_two = LinkedList()

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 3 } -> { 2 } -> NONE"
    assert str(actual) == expected
