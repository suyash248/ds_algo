from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from _collections import defaultdict
import typing

T = typing.TypeVar('T')

class Vertex(typing.Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.__adjacent_vertices__: typing.Set[Vertex] = set()

    def add_adjacent_vertex(self, vertex: Vertex[T]):
        self.__adjacent_vertices__.add(vertex)

    def get_all_adjacent_vertices(self) -> typing.Tuple[Vertex[T], ...]:
        """
        To get all adjacent vertices of given `vertex`

        :return: A tuple of all adjacent vertices.
        """
        return tuple(self.__adjacent_vertices__)

    def __hash__(self):
        return self.data.__hash__()

    def __eq__(self, other: Vertex):
        if other is None: return False
        return self.data == other.data

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.data.__str__()

class Edge(object):
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight=None, is_directed: bool = False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.is_directed = is_directed

    def __hash__(self):
        return hash((self.vertex1, self.vertex2))

    def __eq__(self, other: Edge):
        if other is None: return False
        return (self.vertex1, self.vertex2) == (other.vertex1, other.vertex2)

    def __str__(self):
        return "{}-{}->{}".format(self.vertex1.__str__(), self.weight if self.weight else '', self.vertex2.__str__())

    def __repr__(self):
        return self.__str__()

class Graph(typing.Generic[T]):
    def __init__(self):
        self.__graph__: dict[Vertex: typing.Set[Edge]] = defaultdict(set)
        self.__all_vertices__: typing.Dict[T, Vertex[T]] = dict()
        self.__all_edges__: typing.Set[Edge] = set()

    def add_edge(self, from_vertex_data: T, to_vertex_data: T, weight=None, is_directed: bool = False):
        """
        Creates an @Edge from a vertex corresponding to `from_vertex_data` to a vertex corresponding to `to_vertex_data`.

        e.g. **(from_vertex ---- (weight) ----> to_vertex)**

        If @is_directed is *False*, then reverse @Edge is also created

        e.g. **(to_vertex ---- (weight) ----> from_vertex)**

        :param from_vertex_data:
        :param to_vertex_data:
        :param weight:
        :param is_directed:
        """
        vertex1: Vertex = self.__all_vertices__.setdefault(from_vertex_data, Vertex(from_vertex_data))
        vertex2: Vertex = self.__all_vertices__.setdefault(to_vertex_data, Vertex(to_vertex_data))

        edge = Edge(vertex1, vertex2, weight=weight, is_directed=is_directed)
        self.__all_edges__.add(edge)

        self.__graph__[vertex1].add(edge)

        vertex1.add_adjacent_vertex(vertex2)

        if not is_directed:
            edge2 = Edge(vertex2, vertex1, is_directed)
            self.__all_edges__.add(edge2)

            self.__graph__[vertex2].add(edge2)
            vertex2.add_adjacent_vertex(vertex1)

    def get_all_vertices(self) -> typing.List[typing.Tuple[T, Vertex[T]]]:
        """
        To get all vertices along with the data.

        :return: A list of tuples, each tuple is a pair of vertex data and vertex.
        e.g. [(v1_data, vertex1), (v2_data, vertex2), .... (vN_data, vertexN)]
        """
        return [(data, ver) for data, ver in self.__all_vertices__.items()]

    def get_all_edges(self) -> typing.Tuple[Edge]:
        """
        To get all edges.

        :return: A tuple of edges.
        """
        return tuple(self.__all_edges__)

    def __str__(self):
        graph_str = []
        for vertex, edges in self.__graph__.items():
            vertex_str = vertex.__str__()
            edges_str = set(map(lambda e: e.__str__(), edges))
            graph_str.append('{vertex}: {edges}'.format(vertex=vertex_str, edges=', '.join(edges_str)))
        return '\n'.join(graph_str)

    def __repr__(self):
        return self.__str__()

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

    # a: a-->b, a-->c
    # b: b-->a, b-->d, b-->e
    # e: e-->b, e-->d
    # d: d-->e, d-->b, d-->c
    # c: c-->d, c-->a
    print(graph1)

    all_vertices = graph1.get_all_vertices()
    all_edges = graph1.get_all_edges

    # (a-->c, d-->c, b-->e, b-->a, c-->d, b-->d, d-->b, e-->d, c-->a, e-->b, d-->e, a-->b)
    print("\nAll edges: ", all_edges)

    # a (c, b)
    # b (a, d, e)
    # e (d, b)
    # d (e, c, b)
    # c (a, d)
    print("\nAdjacent vertices: ")
    for data, v in all_vertices: print(v, v.get_all_adjacent_vertices())

    print('\n' + '#'*100 + '\n')

    graph2 = Graph()
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 3)

    print(graph2)
    all_vertices = graph2.get_all_vertices()
    all_edges = graph2.get_all_edges

    # (0-->1, 1-->2, 3-->2, 3-->3, 2-->1, 2-->0, 2-->3, 1-->0, 0-->2)
    print("\nAll edges: ", all_edges)

    # 0 (1, 2)
    # 1 (0, 2)
    # 2 (0, 1, 3)
    # 3 (2, 3)
    print("\nAdjacent vertices: ")
    for data, v in all_vertices: print(v, v.get_all_adjacent_vertices())