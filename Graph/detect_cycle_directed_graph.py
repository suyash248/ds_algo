from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from collections import namedtuple, defaultdict
import typing
from Graph.graph import Graph, Vertex

T = typing.TypeVar('T')

COLOR = namedtuple('COLOR', 'name')
COLOR.__new__.__defaults__ = ('WHITE',) # by default every vertex is of white color, so default value is set to `WHITE`.

# WHITE -> Vertex is unvisited. Initially all the vertices are of WHITE color.
WHITE: COLOR = COLOR(name='WHITE')

# GREY -> Vertex is in recursion stack. i.e. It's getting visited along with adjacent vertices.
GREY: COLOR = COLOR(name='GREY')

# BLACK -> Vertex is visited completely along with it's adjacent vertices, and it's removed from the recursion stack.
BLACK: COLOR = COLOR(name='BLACK')

# https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/
# Time complexity: O(V+E)
def has_cycle_directed(graph: Graph[T]) -> typing.Tuple[bool, typing.List[Vertex[T]]]:
    all_data_vertex_mapping: typing.Dict[T, Vertex[T]] = dict(graph.get_all_vertices())
    vertex_color_mapping: typing.Dict[T, COLOR] = defaultdict(COLOR) # by default every vertex has white color
    vertex_parent_mapping: typing.Dict[Vertex[T], Vertex[T]] = dict()

    def __has_cycle__(vertex: Vertex[T], vertex_color_mapping: typing.Dict[T, COLOR]) -> bool:
        vertex_color_mapping[vertex.data] = GREY
        for adjacent_ver in vertex.get_all_adjacent_vertices():
            # If adjacent_ver/neighbour is of GREY color, then graph has the cycle.

            vertex_parent_mapping[adjacent_ver] = vertex
            # Algo:
            # If color[adjacent_vertex] is BLACK:
            #   continue
            # If color[adjacent_vertex] is GREY:
            #   return True
            # If __has_cycle__(adjacent_ver, vertex_color_mapping): # checking it's descendants/adjacent vertex
            #   return True

            if vertex_color_mapping[adjacent_ver.data] == GREY or \
                    (vertex_color_mapping[adjacent_ver.data] == WHITE
                     and __has_cycle__(adjacent_ver, vertex_color_mapping)
                    ):
                return True
        vertex_color_mapping[vertex.data] = BLACK
        return False

    def get_cyclic_path(vertex: Vertex[T], vertex_parent_mapping: typing.Dict[Vertex[T], Vertex[T]]) -> typing.List[Vertex[T]]:
        """
        :param vertex: Starting vertex of the cycle.
        :param vertex_parent_mapping: Dict containing `vertex` to `immediate parent` mapping.

        :return: Returns an array of vertices which forms a cycle.
        """
        start_vertex: Vertex[T] = vertex
        curr_vertex: Vertex[T] = None

        # ver: A
        # vertex_parent_mapping: {B: A, C: B, E: C, A: C}
        # cycle_path: [A, B, C, A] -> reverse it to get the cyclic path
        cycle_path: typing.List[Vertex[T]] = []
        while curr_vertex != start_vertex:
            if curr_vertex is None:
                curr_vertex = start_vertex
            cycle_path.append(curr_vertex)
            curr_vertex = vertex_parent_mapping[curr_vertex]
        cycle_path.append(curr_vertex)
        return cycle_path[::-1]

    for data, ver in all_data_vertex_mapping.items():
        # Checks for all WHITE vertices one by one.
        if vertex_color_mapping[data] == WHITE:
            if __has_cycle__(ver, vertex_color_mapping):
                # Cycle is found starting at vertex `ver`
                cycle_path = get_cyclic_path(ver, vertex_parent_mapping)
                return True, cycle_path
    return False, []

if __name__ == '__main__':
    #
    #    ⟶ B ⟶ D ⟵ F
    #   |    |     |    |
    #   A    ⭣    ⭣    ⭣
    #   ⭡___ C ⟶ E     G
    #

    # A - C - B - A
    # C - B - A - C

    graph1 = Graph()
    graph1.add_edge('A', 'B', is_directed=True)
    graph1.add_edge('B', 'C', is_directed=True)     # Replace edge B -> C to B -> G it to remove cycle.
    # graph1.add_edge('B', 'G', is_directed=True)
    graph1.add_edge('B', 'D', is_directed=True)
    graph1.add_edge('C', 'A', is_directed=True)
    graph1.add_edge('C', 'E', is_directed=True)
    graph1.add_edge('D', 'E', is_directed=True)
    graph1.add_edge('F', 'D', is_directed=True)
    graph1.add_edge('F', 'G', is_directed=True)

    # A: A-->B
    # B: B-->D, B-->C
    # C: C-->E, C-->A
    # D: D-->E
    # F: F-->D, F-->G
    print('Graph:')
    print(graph1, '\n')

    is_cycle_present, cyclic_path = has_cycle_directed(graph1)
    if is_cycle_present:
        print("Cycle is present:", cyclic_path)
    else:
        print("Cycle is NOT present.")