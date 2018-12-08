from Array import swap
from Heap.BinaryHeap import Heap
from copy import deepcopy

class MaxHeap(Heap):

    # Time Complexity: O(log(n))
    def max_heapify(self, index):
        """
        Algorithm: We move downwards(bottom) in the heap in each step until heap is in it's correct form.

        Max-Heapify (A, i):
            left = 2*i // = means "assignment"
            right = 2*i + 1
            largest = i

            if left < len(A) and A[left] > A[largest] then:
                largest = left
            if right < len(A) and A[right] > A[largest] then:
                largest = right

            if largest != i then:
                swap A[i] and A[largest]
                Max-Heapify(A, largest)
        :param index:
        :return:
        """
        l_idx = MaxHeap.left(index)
        r_idx = MaxHeap.right(index)
        largest = index

        if l_idx < self.capacity and self.get(l_idx) is not None and self.get(l_idx) > self.get(largest):
            largest = l_idx
        if r_idx < self.capacity and self.get(r_idx) is not None and self.get(r_idx) > self.get(largest):
            largest = r_idx

        if largest != index:
            swap(self.harr, largest, index)
            self.max_heapify(largest)

    # Time Complexity: O(n)
    # https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
    def build_heap(self, harr):
        """
        Build-Max-Heap (A):
            for i=floor(length[A]/2); i<=0; i--:
                Max-Heapify(A, i)
        :param harr:
        :return:
        """
        if len(harr) > self.capacity:
            print('''Can't build heap as the array contains {} elements, 
                        which is more than specified capacity({}) of heap'''.format(len(harr), self.capacity))

        self.harr = harr
        self.heap_size = len(harr)
        half = int(self.heap_size / 2)

        for idx in range(half, -1, -1): # for idx=half; idx<=0; idx++
            self.max_heapify(idx)

    # Time Complexity: O(log(n))
    def insert(self, elt):
        if self.is_full():
            print("Heap is full, can't insert key")
            return False

        # First insert the new key at the end.
        self.harr.append(elt)
        self.heap_size += 1
        elt_idx = self.heap_size - 1

        # Fix the max heap property if it is violated.
        # Algorithm: We move upwards(top) step-by-step until heap is in it's correct form.
        # while parent(elt) >=0 and harr[parent(elt)] < elt:
        #   swap(parent, elt)
        #   index(elt) = parent(elt)
        while Heap.parent(elt_idx) >= 0 and self.get(Heap.parent(elt_idx)) < elt:
            swap(self.harr, Heap.parent(elt_idx), elt_idx)
            elt_idx = Heap.parent(elt_idx)
        return True

    # Time Complexity: O(1)
    def get_max(self):
        if self.is_empty():
            print("Heap is empty")
            return False
        return deepcopy(self.harr[0])

    # Time Complexity: O(log(n))
    def delete_max(self):
        if self.is_empty():
            print("Heap is empty")
            return False

        root = self.harr[0]

        # Store last element at root and then heapify to maintain the heap property.
        self.harr[0] = self.harr[self.heap_size - 1]
        self.max_heapify(0)
        self.heap_size -= 1
        return deepcopy(root)

    def heap_arr(self):
        return deepcopy(self.harr)

    def delete(self, idx):
        pass

if __name__ == "__main__":
    harr = [3, 2, 15, 5, 4, 45]
    harr_copy = deepcopy(harr)
    mh = MaxHeap(12)
    mh.build_heap(harr)

    print("Array {} is converted to Max-Heap {}".format(harr_copy, harr))

    elt = 1
    mh.insert(elt)
    print("Inserted {}:".format(elt), harr)

    d_elt = mh.delete_max()
    print("Deleted maximum element(root)=>{}:".format(d_elt), harr)

    #mh.print_heap()
