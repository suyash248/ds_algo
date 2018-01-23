from copy import deepcopy
from sys import maxint
from Tree.segment_tree.base_segment_tree import SegmentTree


class MinRangeSegmentTree(SegmentTree):

    def __init__(self, input_arr):
        super(MinRangeSegmentTree, self).__init__(input_arr)

    # Time complexity: O(n)
    # Space complexity: O(n)
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

    # Time complexity: O(log(n))
    def __range_min_query__(self, qs, qe, low, high, pos):
        # Complete overlap, query range (qs, qe) is completely overlapping (low, high). e.g. (0, 4) (1, 3)
        # return current value i.e. at index `pos`
        if qs <= low and qe >= high:
            return self.seg_tree_arr[pos]

        # No overlap, query range (qs, qe) is not overlapping (low, high). e.g. (3, 4) (0, 2)
        # Return max
        elif qs > high or qe < low:
            return maxint

        # Partial overlap, query range (qs, qe) is partially overlapping (low, high). e.g. (3, 5) (1, 3)
        # Go recursively in left & right subtree.
        else:
            mid = (low + high)/2
            return min(
                self.__range_min_query__(qs, qe, low, mid, 2*pos + 1),
                self.__range_min_query__(qs, qe, mid+1, high, 2*pos + 2)
            )

    def range_min_query(self, qs, qe):
        min_elt = self.__range_min_query__(qs, qe, 0, len(self.input_arr)-1, 0)
        return min_elt

    # Time complexity: O(log(n))
    def __update_value__(self, i, diff, low, high, pos):
        # If the input index `i` lies outside the range of this segment (low, high),
        # return
        if i < low or i > high:
            return

        # Leaf node: low and high are same,
        # update it's value.
        if low == high:
            if low == i: # or high == i, as low & high are same
                self.seg_tree_arr[pos] += diff

        # If the input index `i` lies under the range of this segment (low, high), i.e.
        # low <= i && i <= high && low != high
        else:
            mid = (low + high)/2
            self.__update_value__(i, diff, low, mid, 2 * pos + 1)
            self.__update_value__(i, diff, mid + 1, high, 2 * pos + 2)
            self.seg_tree_arr[pos] = min(
                self.seg_tree_arr[2 * pos + 1], self.seg_tree_arr[2 * pos + 2]
            )

    def update_value(self, i, diff):
        self.__update_value__(i, diff, 0, len(self.input_arr)-1, 0)
        return deepcopy(self.seg_tree_arr)

if __name__ == '__main__':
    input_arr = [1, 4, -1, 0]
    seg_tree_obj = MinRangeSegmentTree(input_arr)
    seg_tree_arr = seg_tree_obj.build_tree()

    print "\n---------- Before modification ----------\n"
    print "Min-Range-Segment tree is:", seg_tree_arr

    qs = 0; qe = 2
    min_elt = seg_tree_obj.range_min_query(qs, qe)
    print "Minimum element in range ({}, {}) is {}".format(qs, qe, min_elt)

    modify_index = 2; diff = 3
    print "\n---------- After modification (Adding {} at index {}) ----------\n".format(diff, modify_index)
    seg_tree_arr_modified = seg_tree_obj.update_value(modify_index, diff)
    print "Min-Range-Segment tree is:", seg_tree_arr_modified
    qs = 0; qe = 2
    min_elt = seg_tree_obj.range_min_query(qs, qe)
    print "Minimum element in range ({}, {}) is {}".format(qs, qe, min_elt)
