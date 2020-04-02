from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import typing
from Graph.graph import Graph, Vertex

T = typing.TypeVar('T')

'''
Breadth-First-Search
'''
def BFS(graph: Graph[T], source_vertex_data: T) -> typing.List[Vertex[T]]:
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.get_all_vertex())

    bfs: typing.List[Vertex[T]] = []
    visited: typing.Dict[T, bool] = dict()
    q: typing.List[Vertex[T]] = list()

    source_vertex: Vertex[T] = all_data_vertex_mapping.get(source_vertex_data)
    if source_vertex_data is None:
        print('Invalid vertex: {}'.format(source_vertex_data))
        return []

    q.append(source_vertex)
    visited[source_vertex_data] = True
    while len(q) > 0:  # while q is not empty
        popped_vertex: Vertex[T] = q.pop(0)
        bfs.append(popped_vertex)

        for ver in popped_vertex.get_all_adjacent_vertex():
            if not visited.get(ver.data, False):  # visited.get(ver.data, False) == False
                visited[ver.data] = True
                q.append(ver)
    return bfs


'''
Depth-First-Search
'''
def DFS(self):
    pass

if __name__ == '__main__':
    # a -- b
    # |    |  \
    # |    |   e
    # |    |  /
    # c -- d

    graph1 = Graph()
    graph1.add_edge('a', 'b', is_directed=False)
    graph1.add_edge('b', 'e', is_directed=False)
    graph1.add_edge('b', 'd', is_directed=False)
    graph1.add_edge('e', 'd', is_directed=False)
    graph1.add_edge('d', 'c', is_directed=False)
    graph1.add_edge('c', 'a', is_directed=False)

    print(graph1)
    bfs_arr = BFS(graph1, 'b')
    # [b, a, e, d, c]
    print("\nBFS:", bfs_arr)

    print('\n' + '#'*100 + '\n')

    graph2 = Graph()
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 3)

    print(graph2)
    bfs_arr = BFS(graph2, 2)
    # [2, 0, 1, 3]
    print("\nBFS:", bfs_arr)