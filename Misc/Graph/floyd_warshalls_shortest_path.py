from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from sys import maxsize
from typing import TypeVar, List, Dict
from Misc.Graph.graph import Graph, Vertex
from Array import empty_2d_array

T = TypeVar('T')
K = TypeVar('K')


# References:
# https://www.youtube.com/watch?v=oNI0rf2P9gE

# Floyd-Warshall's all pairs shortest path algorithm.
# Dijkstra's algo finds shortest path from source vertex to all other vertices. and it's time complexity is O(E*logV) if
# binary heap is used. To find all pairs shortest path we can use Dijkstra's algo V times, overall time complexity in
# that case will be - O(V*E*logV). Floyd-Warshall's algo performs better in thise case.

# Time complexity: O(V*3)
# Space complexity: O(V*2)
def floyd_warshalls_all_pairs_shortest_path(graph: Graph[T]):
    """
    Considers every vertex one-by-one as source, while every other vertex as middle vertex. e.g.
    vertices: 1, 2, 3, 4
    For vertex 1 consider 2, 3, 4 as middle vertex.
    e.g. distance from 1 -> 4 while considering 2 as middle vertex will be: D[1, 4] = MIN(D[1, 4], (D[1, 2] + D[2, 4]))
    D[i, j] = MIN(D[i, j], (D[i, k], D[k, j])) where k is a middle vertex i.e distance from i to j via k.
    :param graph:
    :return:
    """
    vertex_idx_mapping: Dict[Vertex[T], int] = {vertex: i for i, (data, vertex) in enumerate(graph.vertices)}
    num_vertices: int = len(vertex_idx_mapping)
    distance_matrix: List[List[int]] = empty_2d_array(num_vertices, num_vertices, fill_default=maxsize)

    # populating distance from vertex u to v if there is any direct edge between them.
    for edge in graph.edges:
        idx_u: int = vertex_idx_mapping[edge.vertex1]
        idx_v: int = vertex_idx_mapping[edge.vertex2]
        distance_matrix[idx_u][idx_v] = edge.weight

    for i in range(0, num_vertices):
        # Diagonals...distance from a vertex to itself will be 0.
        distance_matrix[i][i] = 0

    for k in range(0, num_vertices): # distance between i, j while considering k as middle vertex.
        for i in range(0, num_vertices):
            for j in range(0, num_vertices):
                if distance_matrix[i][k] == maxsize or distance_matrix[k][j] == maxsize:
                    continue
                else:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    return distance_matrix, vertex_idx_mapping


if __name__ == '__main__':
    #
    #    ------> D <-------
    #   |      /           |
    # 15|    / 1           | 2
    #   | ⤶               |
    #   A -----> B -----> C
    #   |   3       -2    ▲
    #   |                 |
    #    -----------------
    #           6

    graph: Graph[str] = Graph()
    graph.add_edge('A', 'B', weight=3, is_directed=True)
    graph.add_edge('A', 'C', weight=6, is_directed=True)
    graph.add_edge('A', 'D', weight=15, is_directed=True)
    graph.add_edge('B', 'C', weight=-2, is_directed=True)
    graph.add_edge('C', 'D', weight=2, is_directed=True)
    graph.add_edge('D', 'A', weight=1, is_directed=True)

    print(graph)

    distance_matrix, vertex_idx_mapping = floyd_warshalls_all_pairs_shortest_path(graph)
    idx_vertex_mapping = {idx: v for v, idx in vertex_idx_mapping.items()}

    # V  A  B  C  D
    # A: 0  3  1  3
    # B: 1  0  -2  0
    # C: 3  6  0  2
    # D: 1  4  2  0
    print('\nV ', end=' ')
    for idx in sorted(idx_vertex_mapping):
        print(idx_vertex_mapping[idx].data, end='  ')
    print()
    for i in range(0, len(distance_matrix)):
        print(idx_vertex_mapping[i].data, end=': ')
        for j in range(0, len(distance_matrix)):
            print(distance_matrix[i][j], end='  ')
        print()
    print()

    # Minimum distance from A to A is 0
    # Minimum distance from A to B is 3
    # Minimum distance from A to C is 1
    # Minimum distance from A to D is 3
    #
    # Minimum distance from B to A is 1
    # Minimum distance from B to B is 0
    # Minimum distance from B to C is -2
    # Minimum distance from B to D is 0
    #
    # Minimum distance from C to A is 3
    # Minimum distance from C to B is 6
    # Minimum distance from C to C is 0
    # Minimum distance from C to D is 2
    #
    # Minimum distance from D to A is 1
    # Minimum distance from D to B is 4
    # Minimum distance from D to C is 2
    # Minimum distance from D to D is 0

    for i in range(0, len(distance_matrix)):
        for j in range(0, len(distance_matrix)):
            print("Minimum distance from {} to {} is {}".format(idx_vertex_mapping[i].data, idx_vertex_mapping[j].data,
                                                                distance_matrix[i][j]))
        print()

