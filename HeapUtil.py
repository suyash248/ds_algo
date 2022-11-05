from heapq import heappush, heappop
from functools import total_ordering
from enum import Enum

@total_ordering
class __MinHeapElt__(object):
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

@total_ordering
class __MaxHeapElt__:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

class HeapType(Enum):
    MIN = "MIN"
    MAX = "MAX"

class Heap:
    def __int__(self, heapType: HeapType):
        self._heap_ = []
        self._heapType_ = heapType
        self._heapClass_ = __MinHeapElt__ if heapType == HeapType.MIN else __MaxHeapElt__

    def push(self, data):
        heappush(self._heap_, self._heapClass_(data))

    def pop(self):
        heappop(self._heap_)