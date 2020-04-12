from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from sys import maxsize
from collections import defaultdict
from typing import TypeVar, List, Set, Tuple, Dict
from Graph.graph import Graph, Vertex, Edge
from Graph.dijkstras_shortest_path import find_path_from_source_to_vertex

T = TypeVar('T')
K = TypeVar('K')

# References:
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/BellmanFordShortestPath.java
# https://www.youtube.com/watch?v=-mOEd_3gTK0&list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j&index=7

def relax_edges(edges: Tuple[Edge[T]], vertex_distance_mapping: Dict[Vertex[T], int],
               vertex_parent_mapping: Dict[Vertex[T], Vertex[T]], check_negative_weight_cycle=False) -> bool:
    for edge in edges:
        u: Vertex[T] = edge.vertex1
        v: Vertex[T] = edge.vertex2
        distance_source_to_u: int = vertex_distance_mapping[u]
        distance_source_to_v: int = vertex_distance_mapping[v]

        if distance_source_to_v > (distance_source_to_u + edge.weight):
            if check_negative_weight_cycle:
                return True
            vertex_distance_mapping[v] = vertex_distance_mapping[u] + edge.weight
            vertex_parent_mapping[v] = u
    return False

# Space complexity: O(V)
# Time complexity: For single source shortest path: O(E*V) | For all-pairs shortest path: O(E*V^2) ~ O(V^4)
def bellman_fords_shortest_path(graph: Graph[T], source_vertex_data: T) -> \
        Tuple[bool, Dict[Vertex[T], int], Dict[Vertex[T], Vertex[T]]]:
    """
    Unlike Dijkstra's algo, this algo handles -ve weight cycle also. It can also find -ve weight
    cycle(sum of weights corresponding to all edges forming the cycle is -ve).
    :param graph:
    :param source_vertex_data:
    :return: A tuple containing (has_negative_weight_cycle, vertex_distance_mapping, vertex_parent_mapping)
    """

    vertex_distance_mapping: Dict[Vertex[T], int] = defaultdict(lambda: maxsize)  # vertex_weight_mapping
    vertex_parent_mapping: Dict[Vertex[T], Vertex[T]] = dict()
    source_vertex: Vertex[T] = graph.get_vertex(source_vertex_data)

    vertex_distance_mapping[source_vertex] = 0
    vertex_parent_mapping[source_vertex] = None

    # Relax all the edges (V-1)th time.
    # Why (V-1) times? - https://www.youtube.com/watch?v=-mOEd_3gTK0&feature=youtu.be&list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j&t=785
    for i in range(0, len(graph.vertices)-1):   # run it (V-1) times... for i=0: i<(V-1); i++
        relax_edges(graph.edges, vertex_distance_mapping, vertex_parent_mapping)

    # Relax all the edges for one more time(Vth time) to check if there is any -ve weight cycle present.
    has_negative_weight_cycle: bool = relax_edges(graph.edges, vertex_distance_mapping, vertex_parent_mapping,
                                                  check_negative_weight_cycle=True)
    if has_negative_weight_cycle:
        return has_negative_weight_cycle, dict(), dict()

    return has_negative_weight_cycle, vertex_distance_mapping, vertex_parent_mapping


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

    graph1: Graph[str] = Graph()
    graph1.add_edge('A', 'B', weight=5)
    graph1.add_edge('A', 'D', weight=9)
    graph1.add_edge('A', 'E', weight=2)
    graph1.add_edge('B', 'C', weight=2)
    graph1.add_edge('C', 'D', weight=3)
    graph1.add_edge('D', 'F', weight=2)
    graph1.add_edge('E', 'F', weight=3)

    print("\nGraph:")
    print(graph1)

    source_vertex_data: str = 'A'
    has_negative_weight_cycle, vertex_distance_mapping, vertex_parent_mapping = bellman_fords_shortest_path(graph1,
                                                                                                            source_vertex_data)
    # False
    print("Does graph has -ve weight cycle? :", has_negative_weight_cycle)

    if not has_negative_weight_cycle:
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

        target_vertex_data: str = 'D'
        path: List[str] = find_path_from_source_to_vertex(target_vertex_data, vertex_parent_mapping)

        # Path from A to D:  ['A', 'E', 'F', 'D']
        print("\nPath from {} to {}: ".format(source_vertex_data, target_vertex_data), path)

    ################################################################################################

    print("\n" + "#" * 75 + "\n")

    #
    #             2
    #        3 -----➤ 4 <------
    #        ▲         |       |
    #        |       2 |       | 1
    #      6 |         ▼       |
    #        0         5 ------
    #      4 | ↘ 5     ▲
    #        |    ↘    | 4
    #        ▼       ↘ |
    #        1 -----➤ 2
    #            -3
    #

    graph2: Graph[int] = Graph()
    graph2.add_edge(0, 1, weight=4, is_directed=True)
    graph2.add_edge(0, 2, weight=5, is_directed=True)
    graph2.add_edge(0, 3, weight=6, is_directed=True)
    graph2.add_edge(1, 2, weight=-3, is_directed=True)
    graph2.add_edge(2, 5, weight=4, is_directed=True)
    graph2.add_edge(3, 4, weight=2, is_directed=True)
    graph2.add_edge(4, 5, weight=2, is_directed=True)
    graph2.add_edge(5, 4, weight=1, is_directed=True)


    print("\nGraph:")
    print(graph2)

    source_vertex_data: int = 0
    has_negative_weight_cycle, vertex_distance_mapping, vertex_parent_mapping = bellman_fords_shortest_path(graph2,
                                                                                                            source_vertex_data)

    # True
    print("Does graph has -ve weight cycle? :", has_negative_weight_cycle)
    if not has_negative_weight_cycle:
        print("\nDistance from {} to each vertex :\n[source --(distance)--> destination]".format(source_vertex_data))
        for ver, dist in vertex_distance_mapping.items():
            print("{} --({})--> {}".format(source_vertex_data, dist, ver))

        print("\n[Vertex --> parent]:")
        for ver, parent in vertex_parent_mapping.items():
            print("{} --> {}".format(ver, parent))

        target_vertex_data: int = 4
        path: List[int] = find_path_from_source_to_vertex(target_vertex_data, vertex_parent_mapping)

        print("\nPath from {} to {}: ".format(source_vertex_data, target_vertex_data), path)

        ################################################################################################

        print("\n" + "#" * 75 + "\n")

        #
        #             2
        #        3 -----➤ 4 <------
        #        ▲         |       |
        #        |       2 |       | 1
        #      6 |         ▼       |
        #        0         5 ------
        #      4 | ↘ 5     ▲
        #        |    ↘    | 4
        #        ▼       ↘ |
        #        1 -----➤ 2
        #            -3
        #

        graph2: Graph[int] = Graph()
        graph2.add_edge(0, 1, weight=4, is_directed=True)
        graph2.add_edge(0, 2, weight=5, is_directed=True)
        graph2.add_edge(0, 3, weight=6, is_directed=True)
        graph2.add_edge(1, 2, weight=-3, is_directed=True)
        graph2.add_edge(2, 5, weight=4, is_directed=True)
        graph2.add_edge(3, 4, weight=2, is_directed=True)
        graph2.add_edge(4, 5, weight=2, is_directed=True)
        graph2.add_edge(5, 4, weight=1, is_directed=True)

        print("\nGraph:")
        print(graph2)

        source_vertex_data: int = 0
        has_negative_weight_cycle, vertex_distance_mapping, vertex_parent_mapping = bellman_fords_shortest_path(graph2,
                                                                                                                source_vertex_data)

        # True
        print("Does graph has -ve weight cycle? :", has_negative_weight_cycle)
        if not has_negative_weight_cycle:
            print(
                "\nDistance from {} to each vertex :\n[source --(distance)--> destination]".format(source_vertex_data))
            for ver, dist in vertex_distance_mapping.items():
                print("{} --({})--> {}".format(source_vertex_data, dist, ver))

            print("\n[Vertex --> parent]:")
            for ver, parent in vertex_parent_mapping.items():
                print("{} --> {}".format(ver, parent))

            target_vertex_data: int = 4
            path: List[int] = find_path_from_source_to_vertex(target_vertex_data, vertex_parent_mapping)

            print("\nPath from {} to {}: ".format(source_vertex_data, target_vertex_data), path)


    #################################### -ve weight cycle ######################################

    print("\n" + "#" * 75 + "\n")

    #
    #
    #
    #       1         -6
    #   0 ------> 1 <----3
    #              ↘     ▲
    #             3  ↘   | 2
    #                  ↘ |
    #                    2

    graph3: Graph[int] = Graph()
    graph3.add_edge(0, 1, weight=1, is_directed=True)
    graph3.add_edge(1, 2, weight=3, is_directed=True)
    graph3.add_edge(2, 3, weight=2, is_directed=True)
    graph3.add_edge(3, 1, weight=-6, is_directed=True)


    print("\nGraph:")
    print(graph3)

    source_vertex_data: int = 0
    has_negative_weight_cycle, vertex_distance_mapping, vertex_parent_mapping = bellman_fords_shortest_path(graph3,
                                                                                                            source_vertex_data)

    # True
    print("Does graph has -ve weight cycle? :", has_negative_weight_cycle)
    if not has_negative_weight_cycle:
        print("\nDistance from {} to each vertex :\n[source --(distance)--> destination]".format(source_vertex_data))
        for ver, dist in vertex_distance_mapping.items():
            print("{} --({})--> {}".format(source_vertex_data, dist, ver))

        print("\n[Vertex --> parent]:")
        for ver, parent in vertex_parent_mapping.items():
            print("{} --> {}".format(ver, parent))

        target_vertex_data: int = 4
        path: List[int] = find_path_from_source_to_vertex(target_vertex_data, vertex_parent_mapping)

        print("\nPath from {} to {}: ".format(source_vertex_data, target_vertex_data), path)
