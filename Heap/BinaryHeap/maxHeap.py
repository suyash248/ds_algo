from Array import swap
from Heap import Heap
from copy import deepcopy

class MaxHeap(Heap):

    def max_heapify(self, index):
        """
        Algorithm: We move downwards(bottom) of the heap in each step until heap is in it's correct form.

        Max-Heapify (A, i):
            left = 2*i // = means "assignment"
            right = 2*i + 1
            largest = i

            if left <= heap_length[A] and A[left] > A[largest] then:
                largest = left
            if right <= heap_length[A] and A[right] > A[largest] then:
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

    def build_heap(self, harr):
        """
        Build-Max-Heap (A):
            for i=floor(length[A]/2); i<=0; i--:
                Max-Heapify(A, i)
        :param harr:
        :return:
        """
        if len(harr) > self.capacity:
            print '''Can't build heap as the array contains {} elements, 
                        which is more than specified capacity({}) of heap'''.format(len(harr), self.capacity)

        self.harr = harr
        self.heap_size = len(harr)
        half = self.heap_size / 2

        for idx in xrange(half, -1, -1): # for idx=half; idx<=0; idx++
            self.max_heapify(idx)

    def insert(self, elt):
        if self.is_full():
            print "Heap is full, can't insert key"
            return False

        self.harr.append(elt)
        self.heap_size += 1
        elt_idx = self.heap_size - 1

        # Algorithm: We move upwards(top) step-by-step until heap is in it's correct form.
        # while parent(elt) >=0 and harr[parent(elt)] > elt:
        #   swap(parent, elt)
        #   index(elt) = parent(elt)
        while Heap.parent(elt_idx) >= 0 and self.get(Heap.parent(elt_idx)) < elt:
            swap(self.harr, Heap.parent(elt_idx), elt_idx)
            elt_idx = Heap.parent(elt_idx)

    def delete(self, idx):
        pass

    def delete_max(self):
        if self.capacity <= 0:
            print "Heap is empty"
            return False

        root = self.harr[0]

        if self.capacity == 1:
            self.harr = []
        else:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.max_heapify(0)
        self.heap_size -= 1
        return root

if __name__ == "__main__":
    harr = [3, 2, 15, 5, 4, 45]
    harr_copy = deepcopy(harr)
    mh = MaxHeap(12)
    mh.build_heap(harr)

    print "Array {} is converted to Max-Heap {}".format(harr_copy, harr)

    elt = 1
    mh.insert(elt)
    print "Inserted {}:".format(elt), harr

    d_elt = mh.delete_max()
    print "Deleted maximum element(root)=>{}:".format(d_elt), harr

    #mh.print_heap()
