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
