from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from typing import Tuple, TypeVar, Dict
from Graph.graph import Graph, Vertex, Edge
from Graph.disjoint_set import DisjointSet, Node

T = TypeVar('T')

# References -
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/CycleUndirectedGraph.java
# https://www.youtube.com/watch?v=n_t0a_8H8VY
def detect_cycle_using_disjoint_set(graph: Graph[T]) -> bool:
    disjoint_set: DisjointSet[T] = DisjointSet()

    all_data_vertex_mapping: Dict[T, Vertex[T]] = dict(graph.get_all_vertices())
    for data, vertex in all_data_vertex_mapping.items():
        disjoint_set.make_set(data)

    edges: Tuple[Edge[T], ...] = graph.get_all_undirected_edges()
    for edge in edges:
        node1: Node[T] = disjoint_set.find_set(edge.vertex1.data)
        node2: Node[T] = disjoint_set.find_set(edge.vertex2.data)

        # If both vertices belong to same set, then there is a cycle.
        if node1 == node2:
            return True
        disjoint_set.union(node1.data, node2.data)

    return False

# TODO
def detect_cycle_using_DFS(graph: Graph[T]) -> bool:
    pass

# TODO
def detect_cycle_using_BFS(graph: Graph[T]) -> bool:
    pass


if __name__ == '__main__':
    graph1: Graph[str] = Graph()
    graph1.add_edge('A', 'B', reverse=False)
    graph1.add_edge('B', 'C', reverse=False)
    graph1.add_edge('C', 'A', reverse=False)

    print('Graph:')
    print(graph1, '\n')

    # (B-->A, A-->C, B-->C, C-->A, A-->B, C-->B)
    print("All edges:", graph1.get_all_edges())

    # (B---A, A---C, B---C)
    print("Undirected/unique edges:", graph1.get_all_undirected_edges())

    has_cycle = detect_cycle_using_disjoint_set(graph1)
    print("\nGraph has cycle" if has_cycle else "Graph does NOT have cycle")

    graph2: Graph[int] = Graph()
    graph2.add_edge(0, 1, reverse=False)
    graph2.add_edge(1, 2, reverse=False)
    graph2.add_edge(0, 3, reverse=False)
    graph2.add_edge(3, 4, reverse=False)
    graph2.add_edge(4, 5, reverse=False)
    graph2.add_edge(5, 1, reverse=False)

    print('\n' + '#' * 100 + '\n')

    print('Graph:')
    print(graph2, '\n')

    # (2-->1, 1-->2, 0-->1, 3-->4, 4-->3, 1-->5, 1-->0, 5-->1, 5-->4, 4-->5, 3-->0, 0-->3)
    print("All edges:", graph2.get_all_edges())

    # (2---1, 1---5, 3---0, 3---4, 0---1, 5---4)
    print("Undirected/unique edges:", graph2.get_all_undirected_edges())

    has_cycle = detect_cycle_using_disjoint_set(graph2)
    print("\nGraph has cycle" if has_cycle else "Graph does NOT have cycle")

