from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from typing import Tuple, TypeVar, Dict, Set, List
from Graph.graph import Graph, Vertex, Edge
from Graph.disjoint_set import DisjointSet, Node

T = TypeVar('T')

# References -
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/CycleUndirectedGraph.java
# https://www.youtube.com/watch?v=n_t0a_8H8VY
def detect_cycle_using_disjoint_set(graph: Graph[T]) -> bool:
    disjoint_set: DisjointSet[T] = DisjointSet()

    all_data_vertex_mapping: Dict[T, Vertex[T]] = dict(graph.vertices)
    for data, vertex in all_data_vertex_mapping.items():
        disjoint_set.make_set(data)

    edges: Tuple[Edge[T], ...] = graph.undirected_edges
    for edge in edges:
        node1: Node[T] = disjoint_set.find_set(edge.vertex1.data)
        node2: Node[T] = disjoint_set.find_set(edge.vertex2.data)

        # If both vertices belong to same set, then there is a cycle.
        if node1 == node2:
            return True
        disjoint_set.union(node1.data, node2.data)

    return False

# https://www.youtube.com/watch?v=eCG3T1m7rFY
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
def detect_cycle_using_DFS(graph: Graph[T]) -> bool:
    all_data_vertex_mapping: Dict[T, Vertex[T]] = dict(graph.vertices)
    visited: Set[T] = set()

    def __detect_cycle__(vertex: Vertex[T], parent: Vertex[T], visited: Set[T]):
        visited.add(vertex.data)
        for adjacent_ver in vertex.adjacent_vertices:
            if adjacent_ver.data not in visited:
                if __detect_cycle__(adjacent_ver, vertex, visited):
                    return True
            # adjacent_ver is visited through some other node(ancestor) than it's parent, then there is some other
            # path aslo to the adjacent_ver and that path doesn't contain it's parent. It means there is a cycle.
            elif adjacent_ver != parent:
                return True
        return False

    for data, ver in all_data_vertex_mapping.items():
        if data not in visited:
            if __detect_cycle__(ver, None, visited):
                return True
    return False

# TODO
# https://www.geeksforgeeks.org/detect-cycle-in-an-undirected-graph-using-bfs/
def detect_cycle_using_BFS(graph: Graph[T]) -> Tuple[bool, List[Vertex[T]]]:
    pass

# TODO
# https://www.geeksforgeeks.org/detect-cycle-in-the-graph-using-degrees-of-nodes-of-graph/?ref=rp
def detct_cycle_using_degree(graph: Graph[T]) -> bool:
    pass


if __name__ == '__main__':
    graph1: Graph[str] = Graph()
    graph1.add_edge('A', 'B', reverse=False)
    graph1.add_edge('B', 'C', reverse=False)
    graph1.add_edge('C', 'D', reverse=False)

    print('Graph:')
    print(graph1, '\n')

    # (B-->A, A-->C, B-->C, C-->A, A-->B, C-->B)
    print("All edges:", graph1.edges)

    # (B---A, A---C, B---C)
    print("Undirected/unique edges:", graph1.undirected_edges)

    has_cycle = detect_cycle_using_disjoint_set(graph1)
    print("\nUsing Disjoint set - " + ("Graph has cycle" if has_cycle else "Graph does NOT have cycle"))

    has_cycle = detect_cycle_using_DFS(graph1)
    print("\nUsing DFS - " + ("Graph has cycle" if has_cycle else "Graph does NOT have cycle"))

    graph2: Graph[int] = Graph()
    graph2.add_edge(0, 1)
    graph2.add_edge(1, 2)
    graph2.add_edge(0, 3)
    graph2.add_edge(3, 4)
    graph2.add_edge(4, 5)
    graph2.add_edge(5, 1)

    print('\n' + '#' * 100 + '\n')

    print('Graph:')
    print(graph2, '\n')

    # (2-->1, 1-->2, 0-->1, 3-->4, 4-->3, 1-->5, 1-->0, 5-->1, 5-->4, 4-->5, 3-->0, 0-->3)
    print("All edges:", graph2.edges)

    # (2---1, 1---5, 3---0, 3---4, 0---1, 5---4)
    print("Undirected/unique edges:", graph2.undirected_edges)

    has_cycle = detect_cycle_using_disjoint_set(graph2)
    print("\nUsing Disjoint set - " + ("Graph has cycle" if has_cycle else "Graph does NOT have cycle"))

    has_cycle = detect_cycle_using_DFS(graph2)
    print("\nUsing DFS - " + ("Graph has cycle" if has_cycle else "Graph does NOT have cycle"))

    detect_cycle_using_BFS(graph2)

