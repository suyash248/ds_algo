from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from _collections import defaultdict
from copy import copy, deepcopy
import typing

T = typing.TypeVar('T')

class Vertex(typing.Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.__adjacent_vertex__: typing.List[Vertex] = list()

    def add_ajacent_vertex(self, vertex: Vertex[T]):
        self.__adjacent_vertex__.append(vertex)

    def get_all_adjacent_vertex(self) -> typing.List[Vertex[T]]:
        return deepcopy(self.__adjacent_vertex__)

    def __hash__(self):
        return self.data.__hash__()

    def __eq__(self, other: Vertex):
        return self.data == other.data

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data

class Edge(object):
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight=None, is_directed: bool = False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.is_directed = is_directed

    def __hash__(self):
        return hash((self.vertex1, self.vertex2))

    def __eq__(self, other: Edge):
        return (self.vertex1, self.vertex2) == (other.vertex1, other.vertex2)

    def __str__(self):
        return "{}-{}->{}".format(self.vertex1.__str__(), self.weight if self.weight else '', self.vertex2.__str__())

    def __repr__(self):
        return self.__str__()

class Graph(typing.Generic[T]):
    def __init__(self):
        self.__graph__: dict[Vertex: typing.Set[Edge]] = defaultdict(set)
        self.__all_vertex__: typing.Dict[T, Vertex[T]] = dict()
        self.__all_edges__: typing.Set[Edge] = set()

    def add_edge(self, from_vertex_data: T, to_vertex_data: T, weight=None, is_directed: bool = False):
        vertex1: Vertex = self.__all_vertex__.setdefault(from_vertex_data, Vertex(from_vertex_data))
        vertex2: Vertex = self.__all_vertex__.setdefault(to_vertex_data, Vertex(to_vertex_data))

        edge = Edge(vertex1, vertex2, weight=weight, is_directed=is_directed)
        self.__all_edges__.add(edge)

        self.__graph__[vertex1].add(edge)

        vertex1.add_ajacent_vertex(vertex2)

        if not is_directed:
            edge2 = Edge(vertex2, vertex1, is_directed)
            self.__all_edges__.add(edge2)

            self.__graph__[vertex2].add(edge2)
            vertex2.add_ajacent_vertex(vertex1)

    def get_all_vertex(self) -> typing.List[Vertex[T]]:
        return deepcopy(list(self.__all_vertex__.values()))

    def get_all_edges(self) -> typing.Set[Edge]:
        return deepcopy(self.__all_edges__)

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

    graph = Graph()
    graph.add_edge('a', 'b', is_directed=False)
    graph.add_edge('b', 'e', is_directed=False)
    graph.add_edge('b', 'd', is_directed=False)
    graph.add_edge('e', 'd', is_directed=False)
    graph.add_edge('d', 'c', is_directed=False)
    graph.add_edge('c', 'a', is_directed=False)

    av = graph.get_all_vertex()
    ae = graph.get_all_edges()
    print(graph)

    for v in av:
        print(v, v.get_all_adjacent_vertex())
