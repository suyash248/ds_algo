from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from _collections import defaultdict
from uuid import uuid4
import typing

T = typing.TypeVar('T')

class Vertex(typing.Generic[T]):
    def __init__(self, data: T):
        self._id_: str = str(uuid4())
        self._data_: T = data
        self._in_degree_: int = 0
        self._out_degree_: int = 0
        self._adjacent_vertices_: typing.Set[Vertex] = set()

    def __add_adjacent_vertex__(self, vertex: Vertex[T]):
        self._adjacent_vertices_.add(vertex)

    @property
    def adjacent_vertices(self) -> typing.Tuple[Vertex[T], ...]:
        """
        To get all adjacent vertices of given `vertex`

        :return: A tuple of all adjacent vertices.
        """
        return tuple(self._adjacent_vertices_)

    @property
    def id(self) -> str: return self._id_

    @property
    def data(self) -> T: return self._data_

    @property
    def in_degree(self) -> int: return self._in_degree_

    @property
    def out_degree(self) -> int: return self._out_degree_

    @property
    def degree(self) -> int: return self._in_degree_ + self._out_degree_

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other: Vertex):
        if other is None: return False
        return self.data == other.data

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.data.__str__()

class Edge(typing.Generic[T]):
    def __init__(self, vertex1: Vertex[T], vertex2: Vertex[T], weight=None, is_directed: bool = False):
        self._vertex1_: Vertex[T] = vertex1
        self._vertex2_: Vertex[T] = vertex2
        self._weight_: int = weight
        self._is_directed_: bool = is_directed

    @property
    def vertex1(self) -> Vertex[T]: return self._vertex1_

    @property
    def vertex2(self) -> Vertex[T]: return self._vertex2_

    @property
    def weight(self) -> int: return self._weight_

    @property
    def is_directed(self) -> bool: return self._is_directed_

    def __hash__(self):
        return hash((self.vertex1.id, self.vertex2.id))

    def __eq__(self, other: Edge[T]):
        if other is None: return False
        return (self.vertex1.id, self.vertex2.id) == (other.vertex1.id, other.vertex2.id)

    def __str__(self):
        return "{}-{}->{}".format(self.vertex1.__str__(), self.weight if self.weight else '', self.vertex2.__str__())

    def __repr__(self):
        return self.__str__()

class Graph(typing.Generic[T]):
    def __init__(self):
        self._graph_: dict[Vertex: typing.Set[Edge]] = defaultdict(set)
        self._vertices_: typing.Dict[T, Vertex[T]] = dict()
        self._edges_: typing.Set[Edge] = set()

    def add_edge(self, from_vertex_data: T, to_vertex_data: T, weight=None, is_directed: bool = False, reverse: bool = True):
        """
        Creates an @Edge from a vertex corresponding to `from_vertex_data` to a vertex corresponding to `to_vertex_data`.

        e.g. **(from_vertex ---- (weight) ----> to_vertex)**

        If @is_directed is *False*, then reverse @Edge is also created

        e.g. **(to_vertex ---- (weight) ----> from_vertex)**

        :param from_vertex_data: source vertex data
        :param to_vertex_data: destination vertex data
        :param weight: weight associated to the edge
        :param is_directed: directed or undirected edge
        :param reverse: defaults to True, which means for undirected edge, for an edge from v1 to v2 there is a
        reverse edge also from v2 to v1
        """
        vertex1: Vertex = self._vertices_.setdefault(from_vertex_data, Vertex(from_vertex_data))
        vertex2: Vertex = self._vertices_.setdefault(to_vertex_data, Vertex(to_vertex_data))

        vertex1._out_degree_ += 1
        vertex2._in_degree_ += 1

        edge = Edge(vertex1, vertex2, weight=weight, is_directed=is_directed)
        self._edges_.add(edge)

        self._graph_[vertex1].add(edge)

        vertex1.__add_adjacent_vertex__(vertex2)

        if not is_directed and reverse:
            edge2 = Edge(vertex2, vertex1, is_directed)
            self._edges_.add(edge2)

            self._graph_[vertex2].add(edge2)
            vertex2.__add_adjacent_vertex__(vertex1)

    @property
    def vertices(self) -> typing.List[typing.Tuple[T, Vertex[T]]]:
        """
        To get all vertices along with the data.

        :return: A list of tuples, each tuple is a pair of vertex data and vertex.
        e.g. [(v1_data, vertex1), (v2_data, vertex2), .... (vN_data, vertexN)]
        """
        return [(data, ver) for data, ver in self._vertices_.items()]

    @property
    def edges(self) -> typing.Tuple[Edge[T], ...]:
        """
        To get all edges.

        :rtype: object
        :return: A tuple of edges.
        """
        return tuple(self._edges_)

    @property
    def all_undirected_edges(self) -> typing.Tuple[Edge[T], ...]:
        """
        To get all undirected edges. i.e. if there is an edge u to v, there won't be an edge v to u

        :rtype: object
        :return: A tuple of edges.
        """
        hm: typing.Dict[T, T] = defaultdict(list)
        undirected_edges: typing.Set[Edge[T]] = set()

        for edge in self._edges_:
            if edge.vertex2.data in hm[edge.vertex1.data] or edge.vertex1.data in hm[edge.vertex2.data]:
                continue
            hm[edge.vertex1.data].append(edge.vertex2.data)
            hm[edge.vertex2.data].append(edge.vertex1.data)
            undirected_edges.add(edge)
        # print(hm)
        return tuple(undirected_edges)

    @property
    def adjecency_list(self):
        adj_list = []
        for data, vertices in self._graph_.items():
            adj_list.append((data, vertices))
        return tuple(adj_list)

    def __str__(self):
        graph_str = []
        for vertex, edges in self._graph_.items():
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

    all_vertices = graph1.vertices
    all_edges = graph1.edges

    # (a-->c, d-->c, b-->e, b-->a, c-->d, b-->d, d-->b, e-->d, c-->a, e-->b, d-->e, a-->b)
    print("\nAll edges: ", all_edges)

    # a (c, b)
    # b (a, d, e)
    # e (d, b)
    # d (e, c, b)
    # c (a, d)
    print("\nAdjacent vertices: ")
    for data, v in all_vertices: print(v, v.adjacent_vertices)

    print('\n' + '#'*100 + '\n')

    graph2 = Graph()
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 0)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 3)

    print(graph2)
    all_vertices = graph2.vertices
    all_edges = graph2.edges

    # (0-->1, 1-->2, 3-->2, 3-->3, 2-->1, 2-->0, 2-->3, 1-->0, 0-->2)
    print("\nAll edges: ", all_edges)

    # 0 (1, 2)
    # 1 (0, 2)
    # 2 (0, 1, 3)
    # 3 (2, 3)
    print("\nAdjacent vertices: ")
    for data, v in all_vertices: print(v, v.adjacent_vertices)

    print(graph2.adjecency_list)