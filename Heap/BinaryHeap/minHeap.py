from Array import swap
from Heap import Heap
from copy import deepcopy

class MinHeap(Heap):

    def min_heapify(self, index):
        """
        Algorithm: We move downwards(bottom) in the heap in each step until heap is in it's correct form.

        Min-Heapify (A, i):
            left = 2*i // = means "assignment"
            right = 2*i + 1
            smallest = i

            if left < len(A) and A[left] < A[smallest] then:
                smallest = left
            if right < len(A) and A[right] < A[smallest] then:
                smallest = right

            if smallest != i then:
                swap A[i] and A[smallest]
                Min-Heapify(A, smallest)

        :param index:
        :return:
        """
        l_idx = MinHeap.left(index)
        r_idx = MinHeap.right(index)
        smallest = index

        if l_idx < self.capacity and self.get(l_idx) is not None and self.get(l_idx) < self.get(smallest):
            smallest = l_idx
        if r_idx < self.capacity and self.get(r_idx) is not None and self.get(r_idx) < self.get(smallest):
            smallest = r_idx

        if smallest != index:
            swap(self.harr, smallest, index)
            self.min_heapify(smallest)

    def build_heap(self, harr):
        """
        Build-Min-Heap (A):
            for i=floor(length[A]/2); i<=0; i--:
                Min-Heapify(A, i)
        :param harr:
        :return:
        """

        if len(harr) > self.capacity:
            print '''Can't build heap as the array contains {} elements, 
                        which is more than specified capacity({}) of heap'''.format(len(harr), self.capacity)

        self.harr = harr
        self.heap_size = len(harr)
        half = self.heap_size/2

        for idx in xrange(half, -1, -1): # for idx=half; idx<=0; idx++
            self.min_heapify(idx)
        return deepcopy(self.harr)

    def insert(self, elt):
        if self.is_full():
            print "Heap is full, can't insert key"
            return False

        # First insert the new key at the end.
        self.harr.append(elt)
        self.heap_size += 1
        elt_idx = self.heap_size - 1

        # Fix the min heap property if it is violated
        # Algorithm: We move upwards(top) step-by-step until heap is in it's correct form.
        # while parent(elt) >=0 and harr[parent(elt)] > elt:
        #   swap(parent, elt)
        #   index(elt) = parent(elt)
        while Heap.parent(elt_idx) >= 0 and self.get(Heap.parent(elt_idx)) > elt:
            swap(self.harr, Heap.parent(elt_idx), elt_idx)
            elt_idx = Heap.parent(elt_idx)
        return True

    def get_min(self):
        if self.is_empty():
            print "Heap is empty"
            return False
        return deepcopy(self.harr[0])

    def delete(self, idx):
        pass

    def delete_min(self):
        if self.is_empty():
            print "Heap is empty"
            return False

        root = self.harr[0]
        # Store last element at root and then heapify to maintain the heap property.
        self.harr[0] = self.harr[self.heap_size - 1]
        self.min_heapify(0)
        self.heap_size -= 1
        return deepcopy(root)

    def heap_arr(self):
        return deepcopy(self.harr)

if __name__ == "__main__":
    harr = [3, 2, 15, 5, 4, 45]
    harr_copy = deepcopy(harr)

    mh = MinHeap(12)
    mh.build_heap(harr)

    print "Array {} is converted to Min-Heap {}".format(harr_copy, harr)

    elt = 1
    mh.insert(elt)
    print "Inserted {}:".format(elt), harr

    d_elt = mh.delete_min()
    print "Deleted minimum element(root)=>{}:".format(d_elt), harr

    #mh.print_heap()