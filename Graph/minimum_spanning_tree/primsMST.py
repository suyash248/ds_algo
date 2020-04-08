from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import sys
from collections import namedtuple, defaultdict
from typing import TypeVar, Generic, List, Set, Tuple, Dict, Any
from Graph.graph import Graph, Vertex, Edge
from Graph.minimum_spanning_tree.custom_min_heap import MinBinaryHeap, HeapNode

T = TypeVar('T')
K = TypeVar('K')

# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/PrimMST.java
# https://www.youtube.com/watch?v=oP2-8ysT3QQ
def prims_mst(graph: Graph[T]) -> Tuple[int, List[Edge[T]]]:
    min_binary_heap: MinBinaryHeap[Vertex[T], int] = MinBinaryHeap()
    vertex_edge_mapping: Dict[Vertex[T], Edge[T]] = dict()
    total_weight = 0
    adjacency_list: Dict[Vertex[T], Set[Edge[T]]] = graph.adjacency_list
    # start_vertex: Vertex[T] = None

    for i, (data, vertex) in enumerate(graph.vertices):
        if i == 0:
            # Starting from the `start_vertex` and making weight corresponding to it as 0, so that extract_min() will
            # return `start_vertex` from the heap.
            # start_vertex = vertex
            min_binary_heap.push(vertex, 0)
        else:
            min_binary_heap.push(vertex, sys.maxsize)

    while min_binary_heap.size > 0:
        heap_node: HeapNode[Vertex[T], int] = min_binary_heap.extract_min()
        min_vertex: Vertex[T] = heap_node.data
        for connecting_edge in adjacency_list[min_vertex]:
            # connecting_edge: vertex1 -> vertex2 (here vertex1 = min_vertex, vertex2 = connecting.edge.vertex2)
            heap_node: HeapNode[Vertex[T], int] = min_binary_heap.peek(connecting_edge.vertex2)
            if heap_node and connecting_edge.weight < heap_node.weight:
                min_binary_heap.replace_weight(heap_node, connecting_edge.weight)
                vertex_edge_mapping[connecting_edge.vertex2] = connecting_edge
                total_weight += connecting_edge.weight
    return total_weight, list(vertex_edge_mapping.values())

if __name__ == '__main__':
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

    print(graph)

    total_weight, mst_edges = prims_mst(graph)
    print(total_weight, mst_edges)

