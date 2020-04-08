from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import sys
from typing import TypeVar, Generic, List, Set, Tuple, Dict, Any
from Graph.graph import Graph, Vertex, Edge
from Graph.mst.custom_min_heap import MinBinaryHeap, HeapNode

T = TypeVar('T')
K = TypeVar('K')

# https://www.geeksforgeeks.org/kruskals-algorithm-simple-implementation-for-adjacency-matrix/?ref=rp
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# https://www.youtube.com/watch?v=fAuF0EuZVCk
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/KruskalMST.java
# Disjoint set: https://github.com/suyash248/ds_algo/blob/master/Graph/disjoint_set.py

def kruskals_mst(graph: Graph[T]):
    pass