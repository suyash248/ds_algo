class Heap(object):
    def __init__(self, capacity):
        """
        :param capacity: Maximum number of elements, heap can hold.
        """
        self.harr = list()
        self.capacity = capacity
        self.heap_size = 0

    @classmethod
    def left(cls, index):
        """
        :param index:
        :return: Index of left child of harr[index]
        """
        return 2*index + 1

    @classmethod
    def right(cls, index):
        """
        :param index:
        :return: Index of right child of harr[index]
        """
        return 2*index + 2

    @classmethod
    def parent(cls, index):
        """
        :param index:
        :return: Index of parent of harr[index]
        """
        return (index-1)/2

    def get(self, idx):
        """
        :param idx:
        :return: Element present at index `idx`, or `None` if `idx` >= len(harr)
        """
        try:
            elt = self.harr[idx]
        except IndexError:
            elt = None
        return elt

    def is_full(self):
        """
        Checks if heap can hold new element anymore.
        :return: `True`, if heap is full and can NOT hold new element(s).
        """
        return self.capacity == self.heap_size

    def print_heap(self):
        for idx in xrange(0, self.heap_size):
            l_idx = Heap.left(idx)
            r_idx = Heap.right(idx)

            curr_elt = self.get(idx)
            l_elt = self.get(l_idx)
            r_elt = self.get(r_idx)

            print "{current} : left -> {left} | right -> {right}".format(current=curr_elt,
                                                                         left=l_elt, right=r_elt)