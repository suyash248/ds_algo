from heapq import heappush, heappop, heapify
from functools import total_ordering
from enum import Enum
from typing import TypeVar, List, Generic

T = TypeVar('T')


# why total_ordering: https://www.geeksforgeeks.org/python-functools-total_ordering/
@total_ordering
class __MinHeapElt__(Generic[T]):
    def __init__(self, data: T):
        self.data = data

    def __lt__(self, other: T):
        return self.data < other.data

    def __eq__(self, other: T):
        return self.data == other.data


@total_ordering
class __MaxHeapElt__(Generic[T]):
    def __init__(self, data: T):
        self.data = data

    def __lt__(self, other: T):
        return self.data > other.data

    def __eq__(self, other: T):
        return self.data == other.data


class HeapType(Enum):
    MIN = "MIN"
    MAX = "MAX"


class Heap(Generic[T]):
    def __int__(self, heap_type: HeapType):
        self._heap_: List[T] = []
        self._heapType_: HeapType = heap_type
        self._heapClass_ = __MinHeapElt__ if heap_type == HeapType.MIN else __MaxHeapElt__

    def push(self, data: T):
        heappush(self._heap_, self._heapClass_(data))

    def pop(self) -> T:
        return heappop(self._heap_)

    def heapify(self):
        heapify(self._heap_)
