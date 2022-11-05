__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from functools import total_ordering
import heapq


# why total_ordering: https://www.geeksforgeeks.org/python-functools-total_ordering/


@total_ordering
class MaxHeap:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val


@total_ordering
class MinHeap:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val
