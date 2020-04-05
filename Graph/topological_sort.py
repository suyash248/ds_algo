from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import typing
from Graph.graph import Graph, Vertex

T = typing.TypeVar('T')

def topological_sort_using_DFS(graph: Graph[T]):
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.vertices)

    visited: typing.Set[T] = set()
    stack: typing.List[Vertex[T]] = list()

    def __top_sort__(vertex: Vertex[T], visited: typing.Set[T]):
        visited.add(vertex.data)
        for adjacent_ver in vertex.adjacent_vertices:
            if adjacent_ver.data not in visited:
                __top_sort__(adjacent_ver, visited)
        stack.append(vertex)

    for data, ver in all_data_vertex_mapping.items():
        if data not in visited:
            __top_sort__(ver, visited)
    return stack[::-1]

# Kahn's algo: keeps track of degree of each vertex.
# https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
def topological_sort_using_BFS(graph: Graph[T]):
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.vertices)
    vertex_in_degree_mapping = {data: ver.in_degree for data, ver in all_data_vertex_mapping.items()}

    top_order: typing.List[Vertex[T]] = []
    q: typing.List[Vertex[T]] = [v_zero for v_zero in filter(lambda v: v.in_degree == 0, all_data_vertex_mapping.values())]
    count = 0

    while q:
        ver_zero: Vertex[T] = q.pop(0)
        top_order.append(ver_zero)

        for adjacent_ver in ver_zero.adjacent_vertices:
            vertex_in_degree_mapping[adjacent_ver.data] -= 1
            if vertex_in_degree_mapping[adjacent_ver.data] == 0:
                q.append(adjacent_ver)
        count += 1

    if count != len(all_data_vertex_mapping):
        print("Graph has cycle.")
        return False, []

    return True, top_order

if __name__ == '__main__':

    #     H <-- E --------> F --> G
    #           ^           ^
    #           |           |
    #     A --> C <-- B --> D

    graph1 = Graph()
    graph1.add_edge('A', 'C', is_directed=True)
    graph1.add_edge('B', 'C', is_directed=True)
    graph1.add_edge('B', 'D', is_directed=True)
    graph1.add_edge('C', 'E', is_directed=True)
    graph1.add_edge('D', 'F', is_directed=True)
    graph1.add_edge('E', 'F', is_directed=True)
    graph1.add_edge('E', 'H', is_directed=True)
    graph1.add_edge('F', 'G', is_directed=True)

    # A: A-->C
    # B: B-->C, B-->D
    # C: C-->E
    # D: D-->F
    # E: E-->H, E-->F
    # F: F-->G
    print('Graph:')
    print(graph1, '\n')

    all_vertex = graph1.vertices
    # A (C,)
    # C (E,)
    # B (D, C)
    # D (F,)
    # E (F, H)
    # F (G,)
    # H ()
    # G ()
    print("Adjacent vertices:")
    for data, v in all_vertex:
        print(v, v.adjacent_vertices)

    top_sort = topological_sort_using_DFS(graph1)
    # [B, D, A, C, E, H, F, G] or [A, B, C, D, E, F, H, G]
    print("\nTopological sort:", top_sort)

    is_DAG, top_order = topological_sort_using_BFS(graph1)
    if is_DAG:
        print("\nTopological sort:", top_order)
    else:
        print("It's not DAG, Graph contains cycle.", top_order)
