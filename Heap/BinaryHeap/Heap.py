class Heap(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.harr = list()

    @classmethod
    def left(cls, index):
        return 2*index + 1

    @classmethod
    def right(cls, index):
        return 2*index + 2

    @classmethod
    def parent(cls, index):
        return (index-1)/2

    def get(self, idx):
        try:
            elt = self.harr[idx]
        except IndexError:
            elt = None
        return elt

    def size(self):
        return len(self.harr)

    def is_full(self):
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