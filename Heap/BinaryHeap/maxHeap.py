from Array import swap
from Heap import Heap


class MaxHeap(Heap):

    def max_heapify(self, index):
        """
        Algorithm:

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

        half = len(self.harr)/2

        for idx in xrange(half, -1, -1): # for idx=half; idx<=0; idx++
            self.max_heapify(idx)

    def insert(self, elt):
        if self.is_full():
            print "Heap is full, can't insert key"
            return False

        self.harr.append(elt)
        elt_idx = self.size() - 1


        # while parent(elt) >=0 and harr[parent(elt)] > elt:
        #   swap(parent, elt)
        #   index(elt) = parent(elt)
        while Heap.parent(elt_idx) >= 0 and self.get(Heap.parent(elt_idx)) < elt:
            swap(self.harr, Heap.parent(elt_idx), elt_idx)
            elt_idx = Heap.parent(elt_idx)

    def delete(self, idx):
        pass

    def delete_min(self):
        pass

if __name__ == "__main__":
    harr = [3, 2, 15, 5, 4, 45]
    mh = MaxHeap(12)
    mh.build_heap(harr)
    #mh.print_heap()
    print harr

    elt = 1
    mh.insert(elt)
    print "Inserted {elt}:", harr