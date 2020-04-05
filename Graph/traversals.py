from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import typing
from Graph.graph import Graph, Vertex

T = typing.TypeVar('T')

def BFS(graph: Graph[T]) -> typing.List[Vertex[T]]:
    """
    Breadth-First-Search
    Time complexity: O(V+E)
    """
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.vertices)

    bfs: typing.List[Vertex[T]] = []
    visited: typing.Dict[T, bool] = dict()
    q: typing.List[Vertex[T]] = list()

    def __BFS__(vertex: Vertex[T], visited: typing.Dict[T, bool]):
        q.append(vertex)
        visited[vertex.data] = True
        while len(q) > 0:  # while q is not empty
            popped_vertex: Vertex[T] = q.pop(0)
            bfs.append(popped_vertex)

            for adjacent_ver in popped_vertex.adjacent_vertices:
                if not visited.get(adjacent_ver.data, False):  # visited.get(ver.data, False) == False
                    visited[adjacent_ver.data] = True
                    q.append(adjacent_ver)

    # We could randomly start from any vertex and all __BFS__(random_vertex, visited) only once. But then, if graph
    # would be disconnected then, we might miss a few vertex while traversing the graph.
    for data, ver in all_data_vertex_mapping.items():
        if not visited.get(data, False):
            __BFS__(ver, visited)
    return bfs

def DFS_using_stack(graph: Graph[T]) -> typing.List[Vertex[T]]:
    """
    Depth-First-Search using stack
    Time complexity: O(V+E)
    """
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.vertices)

    visited: typing.Dict[T, bool] = dict()
    dfs: typing.List[Vertex[T]] = []
    stack = list()

    def __DFS__(vertex, visited):
        stack.append(vertex)
        visited[vertex.data] = True
        dfs.append(vertex)

        while len(stack) > 0:
            top_ver = stack[-1]
            unvisited_adjacent_ver:Vertex[T] = None
            # Find a unvisited adjacent vertex of top_ver
            for adjacent_ver in top_ver.adjacent_vertices:
                if not visited.get(adjacent_ver.data, False): # visited.get(ver.data, False) == False
                    unvisited_adjacent_ver = adjacent_ver
                    break

            if unvisited_adjacent_ver:
                stack.append(unvisited_adjacent_ver)
                visited[unvisited_adjacent_ver.data] = True
                dfs.append(unvisited_adjacent_ver)

            # If there is no unvisited adjacent vertex of popper_ver is found, then pop the stack
            elif unvisited_adjacent_ver is None and len(stack) > 0:
                stack.pop(-1)

    # We could randomly start from any vertex and all __DFS__(random_vertex, visited) only once. But then, if graph
    # would be disconnected then, we might miss a few vertex while traversing the graph.
    for data, ver in all_data_vertex_mapping.items():
        if not visited.get(data, False):
            __DFS__(ver, visited)
    return dfs

def DFS_recursive(graph: Graph[T]) -> typing.List[Vertex[T]]:
    """
    Depth-First-Search using recursion
    Time complexity: O(V+E)
    """
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.vertices)

    visited: typing.Dict[T, bool] = dict()
    dfs: typing.List[Vertex[T]] = []

    def __DFS__(ver: Vertex[T], visited):
        if not visited.get(ver.data, False):
            visited[ver.data] = True
            dfs.append(ver)

        for adjacent_ver in ver.adjacent_vertices:
            if not visited.get(adjacent_ver.data, False):  # visited.get(ver.data, False) == False
                __DFS__(adjacent_ver, visited)

    # We could randomly start from any vertex and all __DFS__(random_vertex, visited) only once. But then, if graph
    # would be disconnected then, we might miss a few vertex while traversing the graph.
    for data, ver in all_data_vertex_mapping.items():
        if not visited.get(data, False):
            __DFS__(ver, visited)
    return dfs


if __name__ == '__main__':
    # a -- b             x
    # |    |  \        /   \
    # |    |   e      y     z
    # |    |  /
    # c -- d

    graph1 = Graph()
    graph1.add_edge('a', 'b', is_directed=False)
    graph1.add_edge('b', 'e', is_directed=False)
    graph1.add_edge('b', 'd', is_directed=False)
    graph1.add_edge('e', 'd', is_directed=False)
    graph1.add_edge('d', 'c', is_directed=False)
    graph1.add_edge('c', 'a', is_directed=False)
    graph1.add_edge('x', 'y', is_directed=False)
    graph1.add_edge('x', 'z', is_directed=False)

    print(graph1)
    bfs_arr = BFS(graph1)
    # [b, a, e, d, c]
    print("\nBFS:", bfs_arr)

    dfs_arr = DFS_recursive(graph1)
    # [b, d, c, a, e]
    print("\nDFS(Recursive):", dfs_arr)

    dfs_arr = DFS_using_stack(graph1)
    # [b, d, c, a, e]
    print("\nDFS(Using stack):", dfs_arr)

    #########################################################################################

    print('\n' + '#'*100 + '\n')

    graph2 = Graph()
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 3)

    print(graph2)
    bfs_arr = BFS(graph2)
    # [2, 0, 1, 3]
    print("\nBFS:", bfs_arr)

    dfs_arr = DFS_recursive(graph2)
    # [2, 0, 1, 3]
    print("\nDFS(Recursive):", dfs_arr)

    dfs_arr = DFS_using_stack(graph2)
    # [2, 0, 1, 3]
    print("\nDFS(Using stack):", dfs_arr)