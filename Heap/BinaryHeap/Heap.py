class Heap(object):
    def __init__(self, capacity):
        """
        :param capacity: Maximum number of elements, heap can hold.
        """
        self.capacity = capacity
        self.harr = list()

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

    def size(self):
        """
        :return: Number of element(s) present in heap.
        """
        return len(self.harr)

    def is_full(self):
        """
        Checks if heap can hold new element anymore.
        :return: `True`, if heap is full and can NOT hold new element(s).
        """
        return self.capacity == self.size()

    def print_heap(self):
        for idx in xrange(0, len(self.harr)):
            l_idx = Heap.left(idx)
            r_idx = Heap.right(idx)

            curr_elt = self.get(idx)
            l_elt = None if l_idx >= self.capacity else self.harr[l_idx]
            r_elt = None if r_idx >= self.capacity else self.harr[r_idx]

            print "{current} : left -> {left} | right -> {right}".format(current=curr_elt,
                                                                         left=l_elt, right=r_elt)