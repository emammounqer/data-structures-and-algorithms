import pytest
from stack_and_queue.queue import Queue


def test_queue_empty():
    queue = Queue()
    assert queue.front is None
    assert queue.back is None


def test_queue_enqueue_one():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front is not None and queue.front.value == 1
    assert queue.back is not None and queue.back.value == 1


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue


def test_queue_enqueue_multiple_value(queue: Queue):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front and queue.front.value == 1
    assert queue.front.next and queue.front.next.value == 2
    assert queue.front.next.next and queue.front.next.next.value == 3
    assert queue.back and queue.back.value == 3


def test_queue_dequeue_one_value(queue: Queue):
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    first = queue.dequeue()

    assert first == 1
    assert queue.front and queue.front.value == 2
    assert queue.front.next and queue.front.next.value == 3
    assert queue.back and queue.back.value == 3


def test_queue_dequeue_all_except_one(queue: Queue):
    first = queue.dequeue()
    sec = queue.dequeue()

    assert first == 1
    assert sec == 2
    assert queue.front and queue.front.value == 3
    assert queue.front.next is None
    assert queue.back and queue.back.value == 3
    assert queue.back.next is None


def test_queue_dequeue_all(queue: Queue):
    first = queue.dequeue()
    sec = queue.dequeue()
    third = queue.dequeue()

    assert first == 1
    assert sec == 2
    assert third == 3
    assert queue.front is None
    assert queue.back is None


def test_queue_peek(queue: Queue):
    assert queue.peek() == 1
