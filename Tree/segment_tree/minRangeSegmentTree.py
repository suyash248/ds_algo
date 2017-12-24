from copy import deepcopy
from Tree.segment_tree.base_segment_tree import SegmentTree

class MinRangeSegmentTree(SegmentTree):

    def __init__(self, input_arr):
        super(MinRangeSegmentTree, self).__init__(input_arr)

    def __build_tree_util__(self, low, high, pos):
        if low == high:
            self.seg_tree_arr[pos] = self.input_arr[low]
            return
        mid = (low + high)/2
        self.__build_tree_util__(low, mid, 2*pos + 1)
        self.__build_tree_util__(mid + 1, high, 2*pos + 2)
        self.seg_tree_arr[pos] = min(self.seg_tree_arr[2*pos + 1], self.seg_tree_arr[2*pos + 2])

    def build_tree(self):
        self.__build_tree_util__(0, len(self.input_arr)-1, 0)
        return deepcopy(self.seg_tree_arr)

if __name__ == '__main__':
    input_arr = [1, 4, -1, 0]
    seg_tree = MinRangeSegmentTree(input_arr)
    seg_tree_arr = seg_tree.build_tree()
    print seg_tree_arr
