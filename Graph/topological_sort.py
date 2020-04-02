from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import typing
from Graph.graph import Graph, Vertex

T = typing.TypeVar('T')

def topological_sort(graph: Graph[T]):
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.get_all_vertex())

    visited: typing.Set[T] = set()
    stack: typing.List[Vertex[T]] = list()

    def __top_sort__(vertex: Vertex[T], visited: typing.Set[T]):
        visited.add(vertex.data)
        for adjacent_ver in vertex.get_all_adjacent_vertex():
            if adjacent_ver.data not in visited:
                __top_sort__(adjacent_ver, visited)
        stack.append(vertex)

    for data, ver in all_data_vertex_mapping.items():
        if data not in visited:
            __top_sort__(ver, visited)
    return stack[::-1]

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

    all_vertex = graph1.get_all_vertex()
    # A (C,)
    # C (E,)
    # B (D, C)
    # D (F,)
    # E (F, H)
    # F (G,)
    # H ()
    # G ()
    print("Adjacent vertex:")
    for data, v in all_vertex:
        print(v, v.get_all_adjacent_vertex())

    top_sort = topological_sort(graph1)
    # [B, D, A, C, E, H, F, G] or [A, B, C, D, E, F, H, G]
    print("\nTopological sort:", top_sort)