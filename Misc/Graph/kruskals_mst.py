from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from typing import TypeVar, List
from Misc.Graph.graph import Graph, Edge
from Misc.Graph.disjoint_set import DisjointSet, DisjointNode

T = TypeVar('T')
K = TypeVar('K')

# References:
# https://www.youtube.com/watch?v=fAuF0EuZVCk
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/KruskalMST.java
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# Disjoint set: https://github.com/suyash248/ds_algo/blob/master/Graph/disjoint_set.py

# Time complexity: O(ElogE)
# Space complexity: O(E+V)
def kruskals_mst_using_disjoint_set(graph: Graph[T]) -> List[Edge[T]]:
    mst: List[Edge[T]] = []
    sorted_edges: List[Edge[T]] = sorted(graph.edges, key=lambda e: e.weight)
    disjoint_set: DisjointSet[T] = DisjointSet()
    for (data, vertex) in graph.vertices:
        disjoint_set.make_set(data)

    for edge in sorted_edges:
        v1_parent: DisjointNode[T] = disjoint_set.find_set(edge.vertex1.data)
        v2_parent: DisjointNode[T] = disjoint_set.find_set(edge.vertex2.data)

        if v1_parent != v2_parent:
            mst.append(edge)
            disjoint_set.union(v1_parent.data, v2_parent.data)
    return mst

# References:
# https://www.geeksforgeeks.org/kruskals-algorithm-simple-implementation-for-adjacency-matrix/?ref=rp

if __name__ == '__main__':
    #
    #       1     6
    #   A ---- D ---- E
    #   |     /|     /|
    # 3 |  3/  |1  /5 | 2
    #   | /    | /    |
    #   B ---- C ---- F
    #      1      4
    #

    graph: Graph[T] = Graph()
    graph.add_edge('A', 'B', weight=3, reverse=False)
    graph.add_edge('A', 'D', weight=1, reverse=False)
    graph.add_edge('B', 'C', weight=1, reverse=False)
    graph.add_edge('B', 'D', weight=3, reverse=False)
    graph.add_edge('C', 'D', weight=1, reverse=False)
    graph.add_edge('C', 'E', weight=5, reverse=False)
    graph.add_edge('C', 'F', weight=4, reverse=False)
    graph.add_edge('D', 'E', weight=6, reverse=False)
    graph.add_edge('E', 'F', weight=2, reverse=False)

    print("Adjacency list:")
    # A: A--(3)-->B, A--(1)-->D
    # B: B--(3)-->D, B--(1)-->C
    # C: C--(1)-->D, C--(4)-->F, C--(5)-->E
    # D: D--(6)-->E
    # E: E--(2)-->F
    print(graph)
    print('\n' + '#' * 75 + '\n')

    mst_edges: List[Edge] = kruskals_mst_using_disjoint_set(graph)
    total_weight: int = sum(map(lambda e: e.weight, mst_edges))

    # [C--(1)-->B, A--(1)-->D, F--(2)-->E, D--(1)-->C, C--(4)-->F]
    print("\nTotal weight of MST:",total_weight)

    # 9
    print("MST:", mst_edges)