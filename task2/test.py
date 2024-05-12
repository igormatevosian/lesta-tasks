import pytest
from .task2 import CircularBuffer, CircularBufferUsingLinkedList
import time


@pytest.fixture(params=[CircularBuffer, CircularBufferUsingLinkedList])
def buffer(request):
    return request.param(3)


def test_put_and_get(buffer):
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    assert buffer.get() == 1
    assert buffer.get() == 2
    assert buffer.get() == 3


def test_put_overflow(buffer):
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    buffer.put(4)
    assert buffer.get() == 2
    assert buffer.get() == 3
    assert buffer.get() == 4


def test_put_overflow2(buffer):
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    buffer.put(4)
    buffer.put(5)
    buffer.put(6)
    assert buffer.get() == 4
    assert buffer.get() == 5
    assert buffer.get() == 6


def test_get_empty_buffer(buffer):

    assert buffer.get() == None


def test_put_get_cycle(buffer):
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    assert buffer.get() == 1
    buffer.put(4)
    assert buffer.get() == 2
    assert buffer.get() == 3
    assert buffer.get() == 4


def test_put_get_same_value(buffer):
    buffer.put(1)
    buffer.put(1)
    buffer.put(1)
    assert buffer.get() == 1
    assert buffer.get() == 1
    assert buffer.get() == 1


def test_put_get_until_full(buffer):
    buffer.put(1)
    buffer.put(2)
    assert buffer.get() == 1
    buffer.put(3)
    assert buffer.get() == 2
    assert buffer.get() == 3
    buffer.put(4)
    assert buffer.get() == 4


def test_put_get_until_empty(buffer):
    buffer.put(1)
    buffer.put(2)
    buffer.put(3)
    assert buffer.get() == 1
    assert buffer.get() == 2
    assert buffer.get() == 3
    assert buffer.get() == None


def test_performance_comparison():
    start_time = time.time()
    circular_buffer = CircularBuffer(100000)
    for i in range(100000):
        circular_buffer.put(i)
        circular_buffer.get()
    circular_buffer_time = time.time() - start_time

    start_time = time.time()
    circular_buffer_using_linked_list = CircularBufferUsingLinkedList(100000)
    for i in range(100000):
        circular_buffer_using_linked_list.put(i)
        circular_buffer_using_linked_list.get()
    circular_buffer_using_linked_list_time = time.time() - start_time

    assert circular_buffer_using_linked_list_time > circular_buffer_time
