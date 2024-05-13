import random
import time

from typing import MutableSequence

from task3 import sort


class Case:
    def __init__(self, name: str, sequence: MutableSequence):
        self.name = name
        self.sequence = sequence

    def __str__(self) -> str:
        return 'test_{}'.format(self.name)


TEST_CASES = [
    Case(name="small_list", sequence=[
         random.randint(-100000, 100000) for _ in range(1000)]),
    Case(name="big_list", sequence=[
         random.randint(-100000, 100000) for _ in range(1000000)]),
    Case(name="same_items_list", sequence=[1000 for _ in range(1000000)]),
    Case(name="sorted_list", sequence=sorted([
         random.randint(-100000, 100000) for _ in range(1000000)]))

]


def speed_test(test_sample: list):
    l1 = test_sample[:]
    l2 = test_sample[:]

    print("My sort time:")
    start_time = time.time()
    l1 = sort(l1)
    print(time.time() - start_time)

    print("Default python sort time:")
    start_time = time.time()
    l2 = sorted(l2)
    print(time.time() - start_time)

    print(all((i == j for i, j in zip(l1, l2))))


for case in TEST_CASES:
    print(case.name)
    speed_test(case.sequence)
    print('')
