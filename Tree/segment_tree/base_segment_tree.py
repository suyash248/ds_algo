from Array import empty_1d_array
from math import pow, log, ceil

"""
Height of segment tree is log(n) #base 2, and it will be full binary tree.
Full binary tree with height h has at most 2^(h+1) - 1 nodes. Segment tree will have exactly n leaves.
"""

class SegmentTree(object):
    def __init__(self, input_arr):
        self.input_arr = input_arr
        self.n = len(input_arr)
        self.height = ceil(log(self.n, 2))
        # 2^(h+1) - 1, where h = log(n) // base 2
        self.seg_tree_size = int(pow(2, self.height + 1) - 1)
        self.seg_tree_arr = empty_1d_array(self.seg_tree_size)