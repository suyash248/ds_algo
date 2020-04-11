from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from sys import maxsize
from collections import defaultdict
from typing import TypeVar, List, Set, Tuple, Dict
from Graph.graph import Graph, Vertex, Edge
from Graph.custom_min_heap import MinBinaryHeap, HeapNode

T = TypeVar('T')
K = TypeVar('K')

# References:
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/DijkstraShortestPath.java
# https://www.youtube.com/watch?v=lAXZGERcDf4

# Space complexity: O(E+V)
# Time complexity: O(E*log(V))
def dijkstras_shortest_path(graph: Graph[T], source_vertex_data: T = None) \
        -> Tuple[Dict[Vertex[T], int], Dict[Vertex[T], Vertex[T]]]:
    """
    It works for directed as well as undirected graphs unless edge weights are +ve.
    """
    custom_min_heap: MinBinaryHeap[Vertex[T], int] = MinBinaryHeap()
    vertex_distance_mapping: Dict[Vertex[T], int] = defaultdict(lambda : maxsize) # vertex_weight_mapping
    vertex_parent_mapping: Dict[Vertex[T], Vertex[T]] = dict()

    adjacency_list: Dict[Vertex[T], Set[Edge[T]]] = graph.adjacency_list

    for (data, vertex) in graph.vertices:
        if source_vertex_data is None: source_vertex_data = vertex.data
        if vertex.data == source_vertex_data:
            # set distance from source_vertex to itself as 0, first call to extract_min() will pick source_vertex.
            custom_min_heap.push(vertex, 0)
        else:
            custom_min_heap.push(vertex, maxsize)

    while custom_min_heap.size > 0:
        popped_heap_node: HeapNode[Vertex[T], int] = custom_min_heap.extract_min()
        popped_vertex: Vertex[T] = popped_heap_node.data
        popped_vertex_distance: int = popped_heap_node.weight

        vertex_distance_mapping[popped_vertex] = popped_vertex_distance

        if popped_vertex.data == source_vertex_data:
            # Parent of source_vertex will be None
            vertex_parent_mapping[popped_vertex] = None

        # Iterating through all the outgoing edges from popped_vertex to adjacent vertices.
        for connecting_edge in adjacency_list[popped_vertex]:
            adjacent_vertex: Vertex[T] = connecting_edge.vertex2    # adjacent vertex to popped_vertex
            heap_node: HeapNode[Vertex[T], int] = custom_min_heap.peek(adjacent_vertex)

            # If adjacent_vertex is not available in heap, then it has already been processed. and we already found out
            # the shortest path from source vertex to adjacent_vertex
            if heap_node is None: continue

            adjacent_vertex_distance: int = heap_node.weight

            # new distance from source vertex to adjacent_vertex will be -
            # new_distance = distance from popped_vertex to source + distance from adjacent_vertex to popped_vertex
            new_distance: int = vertex_distance_mapping[popped_vertex] + connecting_edge.weight

            if new_distance < adjacent_vertex_distance:
                custom_min_heap.replace_weight(adjacent_vertex, new_distance)

                # popped_vertex is the parent of adjacent_vertex
                vertex_parent_mapping[adjacent_vertex] = popped_vertex

    return vertex_distance_mapping, vertex_parent_mapping


def find_path_from_source_to_vertex(target_vertex_data: T, vertex_parent_mapping: Dict[Vertex[T], Vertex[T]]) -> List[T]:
    vertex_parent_data_mapping: Dict[T, T] = {v.data: p.data if p else None for v, p in vertex_parent_mapping.items()}
    curr: T = target_vertex_data
    path: List[T] = []
    while curr is not None:
        path.append(curr)
        curr = vertex_parent_data_mapping[curr]
    return path[::-1]


if __name__ == '__main__':

    #         2
    #     B ----- C
    #   5 |       | 3
    #     |   9   |
    #     A ----- D
    #   2 |       | 2
    #     |   3   |
    #     E ----- F
    #

    graph: Graph[str] = Graph()
    graph.add_edge('A', 'B', weight=5)
    graph.add_edge('A', 'D', weight=9)
    graph.add_edge('A', 'E', weight=2)
    graph.add_edge('B', 'C', weight=2)
    graph.add_edge('C', 'D', weight=3)
    graph.add_edge('D', 'F', weight=2)
    graph.add_edge('E', 'F', weight=3)

    print("\nGraph:")
    print(graph)

    source_vertex_data: str = 'A'
    vertex_distance_mapping, vertex_parent_mapping = dijkstras_shortest_path(graph, source_vertex_data)

    # A --(0)--> A
    # A --(2)--> E
    # A --(5)--> B
    # A --(5)--> F
    # A --(7)--> C
    # A --(7)--> D
    print("\nDistance from {} to each vertex :\n[source --(distance)--> destination]".format(source_vertex_data))
    for ver, dist in vertex_distance_mapping.items():
        print("{} --({})--> {}".format(source_vertex_data, dist, ver))

    # A --> None
    # B --> A
    # D --> F
    # E --> A
    # F --> E
    # C --> B
    print("\n[Vertex --> parent]:")
    for ver, parent in vertex_parent_mapping.items():
        print("{} --> {}".format(ver, parent))

    target_vertex_data = 'D'
    path: List[str] = find_path_from_source_to_vertex(target_vertex_data, vertex_parent_mapping)

    # Path from A to D:  ['A', 'E', 'F', 'D']
    print("\nPath from {} to {}: ".format(source_vertex_data, target_vertex_data), path)





