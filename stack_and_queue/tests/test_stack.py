import pytest
from stack_and_queue.stack import Stack


def test_stack_create_new_stack():
    stack = Stack()
    assert stack.top is None


def test_stack_add_one_node():
    stack = Stack()
    stack.push(1)
    assert stack.top is not None
    assert stack.top.value == 1
    assert stack.top.next is None


def test_stack_add_two_nodes():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top is not None
    assert stack.top.value == 2
    assert stack.top.next is not None
    assert stack.top.next.value == 1
    assert stack.top.next.next is None


@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack


def test_stack_pop_one_node(stack: Stack):
    assert stack.pop() == 3


def test_stack_pop_all_nodes(stack: Stack):
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_peak_one_node(stack: Stack):
    assert stack.peek() == 3


def test_stack_peak_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()


def test_stack_is_empty(stack: Stack):
    assert stack.is_empty() == False


def test_stack_is_empty_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True
