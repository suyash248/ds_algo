from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from typing import TypeVar, Generic, List, Dict, Any, Tuple
from Array import swap

T = TypeVar('T')
K = TypeVar('K')

# https://www.youtube.com/watch?v=oP2-8ysT3QQ
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/BinaryMinHeap.java
# https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
class HeapNode(Generic[T, K]):
    def __init__(self, data: T, weight: K, *args: Tuple[Any], **kwargs: Dict[Any, Any]):
        self.data = data
        self.weight = weight
        self.args = args
        for k, v in kwargs.items(): setattr(self, k, v)

    def __lt__(self, other): return self.weight < other.weight
    def __le__(self, other): return self.weight <= other.weight
    def __gt__(self, other): return self.weight > other.weight
    def __ge__(self, other): return self.weight >= other.weight

    def __eq__(self, other): return self.weight, self.data == other.weight, other.data
    def __hash__(self): return hash((self.weight, self.data))

    def __str__(self): return "{} - {}".format(self.data.__str__(), self.weight.__str__())

    def __repr__(self): return self.__str__()


class MinBinaryHeap(Generic[T]):
    """
    Data structure to support following operations
    extract_min - O(logn)
    push - O(logn)
    contains_key/peek - O(1)
    replace - O(logn)

    It is a combination of binary heap and hash map
    """
    def __init__(self):
        self._harr_: List[HeapNode[T, K]] = []
        self._data_position_mapping_: Dict[T, int] = dict()

    @staticmethod
    def left_child(idx: int) -> int:
        return 2 * idx + 1

    @staticmethod
    def right_child(idx: int) -> int:
        return 2 * idx + 2

    @staticmethod
    def parent(idx: int) -> int:
        return int((idx - 1)/2)

    @property
    def size(self):
        return len(self._harr_)

    def __len__(self): return self.size

    def push(self, data: T, weight: K, *args, **kwargs) -> HeapNode[T, K]:
        heap_node = HeapNode(data, weight, *args, **kwargs)
        self._harr_.append(heap_node)
        curr_idx = len(self._harr_) - 1
        parent_idx = MinBinaryHeap.parent(curr_idx)
        self._data_position_mapping_[data] = curr_idx

        while self._harr_[curr_idx] < self._harr_[parent_idx]:
            self._data_position_mapping_[data] = parent_idx     # Update curr node data index to point to it's parent
            self._data_position_mapping_[self._harr_[parent_idx].data] = curr_idx # Update parent index to point to curr_idx.

            swap(self._harr_, parent_idx, curr_idx)

            curr_idx = parent_idx
            parent_idx = MinBinaryHeap.parent(curr_idx)

        return heap_node

    def min_heapify(self, curr_index: int):
        left_idx = MinBinaryHeap.left_child(curr_index)
        right_idx = MinBinaryHeap.right_child(curr_index)

        left_elt = self._harr_[left_idx]
        right_elt = self._harr_[right_idx]

        smallest_elt_idx = curr_index

        if left_elt < self._harr_[smallest_elt_idx]:
            smallest_elt_idx = left_idx

        if right_elt < self._harr_[smallest_elt_idx]:
            smallest_elt_idx = right_idx

        if smallest_elt_idx != curr_index:
            self._data_position_mapping_[self._harr_[smallest_elt_idx].data] = curr_index
            self._data_position_mapping_[self._harr_[curr_index].data] = smallest_elt_idx
            swap(self._harr_, smallest_elt_idx, curr_index)

    def extract_min(self) -> HeapNode[T, K]:
        if len(self._harr_) == 0:
            return None

        min_idx = 0
        last_idx = -1
        min_heap_node = self._harr_[min_idx]
        last_heap_node = self._harr_[last_idx]

        self._data_position_mapping_.pop(min_heap_node.data)    # Remove first node
        self._data_position_mapping_[last_heap_node.data] = min_idx # Update last_node index to min_idx

        swap(self._harr_, min_idx, last_idx) # Move last node to the first index(min_idx)
        self._harr_.pop(last_idx) # Remove last node
        self.min_heapify(min_idx)
        return min_heap_node

    def peek(self, data: T) -> HeapNode[T, K]:
        idx = self._data_position_mapping_.get(data, None)
        if idx is not None:
            return self._harr_[idx]
        return None

    def replace_weight(self, data: T, new_weight: K) -> True:

        heap_node_idx: int = self._data_position_mapping_.get(data)
        if heap_node_idx is None:
            print("No such element -", data)
            return False

        heap_node: HeapNode[T, K] = self._harr_[heap_node_idx]
        curr_weight = heap_node.weight
        heap_node.weight = new_weight

        curr_idx = heap_node_idx
        parent_idx = MinBinaryHeap.parent(curr_idx)
        if new_weight < curr_weight:
            while self._harr_[curr_idx] < self._harr_[parent_idx]:
                self._data_position_mapping_[data] = parent_idx  # Update curr node data index to point to it's parent
                self._data_position_mapping_[self._harr_[parent_idx].data] = curr_idx  # Update parent index to point to curr_idx.

                swap(self._harr_, parent_idx, curr_idx)
                curr_idx = parent_idx
                parent_idx = MinBinaryHeap.parent(curr_idx)
                # curr_idx, parent_idx = parent_idx, MinBinaryHeap.parent(curr_idx)
        elif new_weight > curr_weight:
            self.min_heapify(curr_idx)

        return True

    def __str__(self):
        s_heap = []

        half = int(self.size / 2)
        for idx in range(0, half):
            l_idx = self.left_child(idx)
            r_idx = self.right_child(idx)

            curr_elt = self._harr_[idx]
            l_elt = self._harr_[l_idx]
            r_elt = self._harr_[r_idx]

            s_heap.append("{current} : left -> {left} | right -> {right}".format(current=curr_elt.__str__(),
                                                                         left=l_elt.__str__(), right=r_elt.__str__()))
        return '\n'.join(s_heap)

    def __repr__(self): return self.__str__()

if __name__ == '__main__':
    heap = MinBinaryHeap()
    heap.push('D', 5)
    heap.push('A', 2)
    heap.push('B', 9)
    heap.push('C', 1)
    heap.push('F', 4)

    print(heap.peek('B'))
    print(heap.replace_weight('B', 3))
    print(heap.peek('B'))
    print("extract min", heap.extract_min())
    print(heap.peek('R'))
    heap.push('G', 2)
    print(heap.replace_weight('G', 6))
    print(heap.peek('G'))
    print(heap)
    # print("extract min", heap.extract_min())
    # print("extract min", heap.extract_min())

