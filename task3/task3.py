import random

from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar, MutableSequence


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...


T = TypeVar('T', bound=Comparable)


def sort(nums: MutableSequence[T]) -> MutableSequence[T]:
    """Sorts a list of numbers using quicksort algorithm.

    Args:
        nums (MutableSequence[T]): List of numbers or objects supporting comparison.

    Returns:
        MutableSequence[T]: Sorted list.
    """
    def quicksort(nums: MutableSequence[T], begin: int, end: int) -> None:
        if begin >= end:
            return

        i, j = begin, end
        pivot = nums[random.randint(begin, end)]

        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        quicksort(nums, begin, j)
        quicksort(nums, i, end)

    quicksort(nums, 0, len(nums)-1)
    return nums
