import time
import random

import pytest

from .task1 import is_even, is_even_bitwise


class Case:
    def __init__(self, num: int, expected: bool):
        self.num = num
        self.expected = expected

    def __str__(self) -> str:
        return 'test_{}'.format(self.num)


TEST_CASES = [
    Case(num=1, expected=False),
    Case(num=2, expected=True),
    Case(num=3, expected=False),
    Case(num=4, expected=True),
    Case(num=5, expected=False),
    Case(num=-1, expected=False),
    Case(num=-2, expected=True),
    Case(num=-3, expected=False),
    Case(num=-4, expected=True),
    Case(num=-5, expected=False),
]

RANDOM_SAMPLE = [random.choice(TEST_CASES).num for _ in range(10_000_000)]

NEGATIVE_TEST_CASES = [
    random.randint(-1000000, 0) for _ in range(10_000_000)
]

BIG_NUMBERS_TEST_CASES = [
    random.randint(0, 100_000_000_000_000) for _ in range(10_000_000)
]


@pytest.mark.parametrize('test_case', TEST_CASES, ids=str)
def test_is_even(test_case: Case) -> None:
    answer = is_even(test_case.num)
    assert answer == test_case.expected


@pytest.mark.parametrize('test_case', TEST_CASES, ids=str)
def test_is_even_bitwise(test_case: Case) -> None:
    answer = is_even_bitwise(test_case.num)
    assert answer == test_case.expected


def test_is_even_performance():
    start_time = time.time()
    for num in RANDOM_SAMPLE:
        is_even(num)
    end_time = time.time()
    print("Время выполнения is_even:", end_time - start_time)


def test_is_even_bitwise_performance():
    start_time = time.time()
    for num in RANDOM_SAMPLE:
        is_even_bitwise(num)
    end_time = time.time()
    print("Время выполнения is_even_bitwise:", end_time - start_time)


def test_is_even_negative_performance():
    start_time = time.time()
    for num in NEGATIVE_TEST_CASES:
        is_even(num)
    end_time = time.time()
    print("Время выполнения is_even для отрицательных:", end_time - start_time)


def test_is_even_bitwise__negative_performance():
    start_time = time.time()
    for num in NEGATIVE_TEST_CASES:
        is_even_bitwise(num)
    end_time = time.time()
    print("Время выполнения is_even_bitwise для отрицательных:",
          end_time - start_time)


def test_is_even_big_numbers_performance():
    start_time = time.time()
    for num in BIG_NUMBERS_TEST_CASES:
        is_even(num)
    end_time = time.time()
    print("Время выполнения is_even для больших чисел:", end_time - start_time)


def test_is_even_bitwise_big_numbers_performance():
    start_time = time.time()
    for num in BIG_NUMBERS_TEST_CASES:
        is_even_bitwise(num)
    end_time = time.time()
    print("Время выполнения is_even_bitwise для больших чисел:",
          end_time - start_time)
