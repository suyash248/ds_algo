from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import sys
from typing import TypeVar, List, Set, Tuple, Dict
from Graph.graph import Graph, Vertex, Edge
from Graph.custom_min_heap import MinBinaryHeap, HeapNode

T = TypeVar('T')
K = TypeVar('K')

# References:
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/PrimMST.java
# https://www.youtube.com/watch?v=oP2-8ysT3QQ

# Space complexity: O(E+V)
# Time complexity: O(E*log(V))
def prims_mst(graph: Graph[T]) -> List[Edge[T]]:
    # Vertex to min edge weight mapping. this is used to pick the vertex having a connecting edge with min. weight by
    # performing extract_min() call.
    # Each element/node(HeapNode) in the heap contains Vertex as data and edge weight.
    min_binary_heap: MinBinaryHeap[Vertex[T], int] = MinBinaryHeap()
    vertex_edge_mapping: Dict[Vertex[T], Edge[T]] = dict()
    adjacency_list: Dict[Vertex[T], Set[Edge[T]]] = graph.adjacency_list

    for i, (data, vertex) in enumerate(graph.vertices):
        if i == 0:
            # Make weight of one node 0 so that this vertex is picked as first vertex .
            min_binary_heap.push(vertex, 0)
        else:
            min_binary_heap.push(vertex, sys.maxsize)

    while min_binary_heap.size > 0:
        popped_heap_node: HeapNode[Vertex[T], int] = min_binary_heap.extract_min()
        for connecting_edge in adjacency_list[popped_heap_node.data]:
            # connecting_edge: vertex1 -> vertex2 (vertex1 = popped_heap_node.data, vertex2 = connecting.edge.vertex2)
            heap_node: HeapNode[Vertex[T], int] = min_binary_heap.peek(connecting_edge.vertex2)

            # If adjacent vertex(connecting_edge.vertex2) exists in min_heap and edge weight is lower. update the weight
            # for `heap_node` in min_heap and add this edge to output(vertex_edge_mapping)
            # against connecting_edge.vertex2.
            if heap_node and connecting_edge.weight < heap_node.weight:
                min_binary_heap.replace_weight(heap_node.data, connecting_edge.weight)

                # Update MST dict
                vertex_edge_mapping[connecting_edge.vertex2] = connecting_edge
    return list(vertex_edge_mapping.values())


# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/?ref=rp
# Time complexity: O(V*2)
# Space complexity: O(E+V)
def prims_mst_v2(graph: Graph[T]) -> List[Edge[T]]:
    # stores vertex --> edge(with min weight mapping).
    vertex_edge_mapping: Dict[Vertex[T], Edge[T]] = dict()
    adjacency_list: Dict[Vertex[T], Set[Edge[T]]] = graph.adjacency_list

    # Vertex to min edge weight mapping. this is used to pick the vertex having a connecting edge with min. weight.
    vertex_edge_weight_mapping: Dict[Vertex[T], int] = dict()

    for i, (data, vertex) in enumerate(graph.vertices):
        if i == 0:
            vertex_edge_weight_mapping[vertex] = 0
        else:
            vertex_edge_weight_mapping[vertex] = sys.maxsize

    while len(vertex_edge_weight_mapping) > 0:
        # Extract(get & pop) vertex with min edge weight from vertex_edge_weight_mapping dict.
        vertex_min_wt_tuple: Tuple[Vertex[T], int] = (None, sys.maxsize)
        for vertex, wt in vertex_edge_weight_mapping.items():
            if wt < vertex_min_wt_tuple[1]:
                vertex_min_wt_tuple = (vertex, wt)
        vertex_with_min_edge_weight: Vertex[T] = vertex_min_wt_tuple[0]
        vertex_edge_weight_mapping.pop(vertex_with_min_edge_weight)

        for connecting_edge in adjacency_list[vertex_with_min_edge_weight]:
            # connecting_edge: vertex1 -> vertex2 (here vertex1 = popped_heap_node.data, vertex2 = connecting.edge.vertex2)
            adj_ver_weight: int = vertex_edge_weight_mapping.get(connecting_edge.vertex2)

            # If adjacent vertex(connecting_edge.vertex2) exists in vertex_edge_weight_mapping and edge weight is lower.
            # update vertex_edge_weight_mapping and add this edge to output(vertex_edge_mapping)
            # against connecting_edge.vertex2.
            if connecting_edge.vertex2 in vertex_edge_weight_mapping and connecting_edge.weight < adj_ver_weight:
                vertex_edge_weight_mapping[connecting_edge.vertex2] = connecting_edge.weight
                vertex_edge_mapping[connecting_edge.vertex2] = connecting_edge

    return list(vertex_edge_mapping.values())


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
    graph.add_edge('A', 'B', weight=3)
    graph.add_edge('A', 'D', weight=1)
    graph.add_edge('B', 'C', weight=1)
    graph.add_edge('B', 'D', weight=3)
    graph.add_edge('C', 'D', weight=1)
    graph.add_edge('C', 'E', weight=5)
    graph.add_edge('C', 'F', weight=4)
    graph.add_edge('D', 'E', weight=6)
    graph.add_edge('E', 'F', weight=2)

    print("Adjacency list:")
    # A: A--(3)-->B, A--(1)-->D
    # B: B--(3)-->D, B--(1)-->C
    # C: C--(1)-->D, C--(4)-->F, C--(5)-->E
    # D: D--(6)-->E
    # E: E--(2)-->F
    print(graph)
    print('\n' + '#' * 75 + '\n')

    mst_edges: List[Edge] = prims_mst(graph)
    total_weight: int = sum(map(lambda e: e.weight, mst_edges))

    # [C--(1)-->B, A--(1)-->D, F--(2)-->E, D--(1)-->C, C--(4)-->F]
    print("\nTotal weight of MST:",total_weight)

    # 9
    print("MST:", mst_edges)

    print('\n' + '#' * 75 + '\n')

    mst_edges: List[Edge] = prims_mst_v2(graph)
    total_weight: int = sum(map(lambda e: e.weight, mst_edges))

    # [C--(1)-->B, A--(1)-->D, F--(2)-->E, D--(1)-->C, C--(4)-->F]
    print("\nTotal weight of MST:", total_weight)

    # 9
    print("MST:", mst_edges)