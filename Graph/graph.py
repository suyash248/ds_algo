from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from _collections import defaultdict
from uuid import uuid4
from typing import TypeVar, Generic, List, Set, Tuple, Dict

T = TypeVar('T')

class Vertex(Generic[T]):
    def __init__(self, data: T):
        self._id_: str = str(uuid4())
        self._data_: T = data
        self._incoming_edges_: List[Edge[T]] = []
        self._outgoing_edges_: List[Edge[T]] = []
        self._adjacent_vertices_: Set[Vertex] = set()

    def __add_adjacent_vertex__(self, vertex: Vertex[T]):
        self._adjacent_vertices_.add(vertex)

    @property
    def adjacent_vertices(self) -> Tuple[Vertex[T], ...]: return tuple(self._adjacent_vertices_)

    @property
    def id(self) -> str: return self._id_

    @property
    def data(self) -> T: return self._data_

    @property
    def incoming_edges(self) -> Tuple[Edge[T], ...]: return tuple(self._incoming_edges_)

    @property
    def outgoing_edges(self) -> Tuple[Edge[T], ...]: return tuple(self._outgoing_edges_)

    @property
    def edges(self) -> Tuple[Edge[T], ...]: return tuple(self._incoming_edges_ + self._outgoing_edges_)

    @property
    def in_degree(self) -> int: return len(self._incoming_edges_)

    @property
    def out_degree(self) -> int: return len(self._outgoing_edges_)

    @property
    def degree(self) -> int: return (self.in_degree + self.out_degree)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other: Vertex):
        if other is None: return False
        return self.data == other.data

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.data.__str__()

class Edge(Generic[T]):
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
        return "{}-{}->{}".format(self.vertex1.__str__(), ('-(' + str(self.weight) + ')-') if self.weight else '-', self.vertex2.__str__())

    def __repr__(self):
        return self.__str__()

class Graph(Generic[T]):
    def __init__(self):
        self._graph_: Dict[Vertex[T], Set[Edge]] = defaultdict(set)
        self._vertices_: Dict[T, Vertex[T]] = dict()
        self._edges_: Set[Edge] = set()

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

        edge = Edge(vertex1, vertex2, weight=weight, is_directed=is_directed)
        self._edges_.add(edge)

        vertex1._outgoing_edges_.append(edge)
        vertex2._incoming_edges_.append(edge)

        self._graph_[vertex1].add(edge)

        vertex1.__add_adjacent_vertex__(vertex2)

        if not is_directed and reverse:
            edge2 = Edge(vertex2, vertex1, weight=weight, is_directed=is_directed)
            self._edges_.add(edge2)

            vertex2._outgoing_edges_.append(edge2)
            vertex1._incoming_edges_.append(edge2)

            self._graph_[vertex2].add(edge2)
            vertex2.__add_adjacent_vertex__(vertex1)

    @property
    def vertices(self) -> Tuple[Tuple[T, Vertex[T]], ...]:
        """
        To get all vertices along with the data.

        :return: A tuple of tuples, each tuple is a pair of vertex data and vertex.
        e.g. ( (v1_data, vertex1), (v2_data, vertex2), .... (vN_data, vertexN) )
        """
        return tuple([(data, ver) for data, ver in self._vertices_.items()])

    @property
    def edges(self) -> Tuple[Edge[T], ...]:
        """
        To get all edges.

        :rtype: object
        :return: A tuple of edges.
        """
        return tuple(self._edges_)

    @property
    def undirected_edges(self) -> Tuple[Edge[T], ...]:
        """
        For an **undirected edge** connecting vertices **U** & **V**, it will either include
        the edge **U-->V** or **V-->U**.

        :return: A tuple of all the undirected edges.
        """
        hm: Dict[T, T] = defaultdict(list)
        undirected_edges: Set[Edge[T]] = set()

        for edge in self._edges_:
            if edge.vertex2.data in hm[edge.vertex1.data] or edge.vertex1.data in hm[edge.vertex2.data]:
                continue
            hm[edge.vertex1.data].append(edge.vertex2.data)
            hm[edge.vertex2.data].append(edge.vertex1.data)
            undirected_edges.add(edge)
        # print(hm)
        return tuple(undirected_edges)

    @property
    def adjacency_list(self) -> Dict[Vertex[T], Set[Edge]]:
        """
        :return: Adjacency list representation of the graph - {v1: {e1, e2}, v2: {e5, e7}, ... vN: {e3, e12}}
        """
        return self._graph_
        # return tuple([(vertex, edges) for vertex, edges in self._graph_.items()])

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
    print()

    # Vertex: a | Degree: (In, Out): (2, 2) | Adjacent vertices: (b, c) | Incoming edges: (b--->a, c--->a) | Outgoing edges: (a--->b, a--->c)
    # Vertex: b | Degree: (In, Out): (3, 3) | Adjacent vertices: (a, d, e) | Incoming edges: (a--->b, e--->b, d--->b) | Outgoing edges: (b--->a, b--->e, b--->d)
    # Vertex: e | Degree: (In, Out): (2, 2) | Adjacent vertices: (b, d) | Incoming edges: (b--->e, d--->e) | Outgoing edges: (e--->b, e--->d)
    # Vertex: d | Degree: (In, Out): (3, 3) | Adjacent vertices: (c, b, e) | Incoming edges: (b--->d, e--->d, c--->d) | Outgoing edges: (d--->b, d--->e, d--->c)
    # Vertex: c | Degree: (In, Out): (2, 2) | Adjacent vertices: (a, d) | Incoming edges: (d--->c, a--->c) | Outgoing edges: (c--->d, c--->a)
    for data, v in all_vertices:
        print(' | '.join(['Vertex: ' + str(v),
                          'Degree: (In, Out): ' + '({}, {})'.format(v.in_degree, v.out_degree),
                          'Adjacent vertices: ' + str(v.adjacent_vertices), 'Incoming edges: ' + str(v.incoming_edges),
                          'Outgoing edges: ' + str(v.outgoing_edges)]))

    print('\n' + '#'*100 + '\n')

    graph2 = Graph()
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 3)

    print(graph2)
    all_vertices = graph2.vertices
    all_edges = graph2.edges

    # (0-->1, 1-->2, 3-->2, 3-->3, 2-->1, 2-->0, 2-->3, 1-->0, 0-->2)
    print("\nAll edges: ", all_edges)
    print()

    # Vertex: 0 | Degree: (In, Out): (2, 2) | Adjacent vertices: (1, 2) | Incoming edges: (1--->0, 2--->0) | Outgoing edges: (0--->1, 0--->2)
    # Vertex: 1 | Degree: (In, Out): (2, 2) | Adjacent vertices: (0, 2) | Incoming edges: (0--->1, 2--->1) | Outgoing edges: (1--->0, 1--->2)
    # Vertex: 2 | Degree: (In, Out): (3, 3) | Adjacent vertices: (0, 1, 3) | Incoming edges: (0--->2, 1--->2, 3--->2) | Outgoing edges: (2--->0, 2--->1, 2--->3)
    # Vertex: 3 | Degree: (In, Out): (3, 3) | Adjacent vertices: (2, 3) | Incoming edges: (2--->3, 3--->3, 3--->3) | Outgoing edges: (3--->2, 3--->3, 3--->3)
    for data, v in all_vertices:
        print(' | '.join(['Vertex: ' + str(v), 'Degree: (In, Out): ' + '({}, {})'.format(v.in_degree, v.out_degree),
              'Adjacent vertices: ' + str(v.adjacent_vertices), 'Incoming edges: ' + str(v.incoming_edges),
               'Outgoing edges: ' + str(v.outgoing_edges)]))


    # {0: {0-->1, 0-->2}, 1: {1-->2, 1-->0}, 2: {2-->3, 2-->1, 2-->0}, 3: {3-->2, 3-->3}}
    print(graph2.adjacency_list)