from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import sys, copy
from collections import defaultdict
from Array import empty_2d_array
from typing import TypeVar, Generic, List, Set, Tuple, Dict, Tuple
from Graph.graph import Graph, Vertex, Edge

T = TypeVar('T')
K = TypeVar('K')

def get_edges(x: int, y: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    adjacent_vertices: List[Tuple[int, int]] = []
    # x+3, y
    if x+3 < rows:
        adjacent_vertices.append((x+3, y))
    if y+3 < cols:
        adjacent_vertices.append((x, y+3))
    if x-3 >= 0:
        adjacent_vertices.append((x-3, y))
    if y-3 >= 0:
        adjacent_vertices.append((x, y-3))

    if x+2 < rows and y+2 < cols:
        adjacent_vertices.append((x+2, y+2))
    if x-2 >= 0 and y-2 >= 0:
        adjacent_vertices.append((x-2, y-2))
    if x+2 < rows and y-2 >= 0:
        adjacent_vertices.append((x+2, y-2))
    if x-2 >= 0 and y+2 < cols:
        adjacent_vertices.append((x-2, y+2))
    return adjacent_vertices

def build_graph(rows: int = 4, cols:int = 4) -> Graph[T]:
    graph: Graph[T] = Graph()
    for i in range(0, rows):
        for j in range(0, cols):
            # print("{}{}".format(i, j), end=' ')
            v1_data: T = '{},{}'.format(i, j)
            adjacent_vertices: List[Tuple[int, int]] = get_edges(i, j, rows, cols)
            for adj_ver in adjacent_vertices:
                v2_data: T = '{},{}'.format(*adj_ver)
                graph.add_edge(v1_data, v2_data, reverse=False)
        # print()
    # print(get_edges(0, 0, rows, cols))
    return graph

def get_adjacent_vertex_with_min_rank(vertex: Vertex[T], visited: Set[T]) -> Tuple[int, Vertex[T]]:
    # visited.add(vertex.data)
    min_rank = sys.maxsize
    vertex_with_min_rank: Vertex[T] = None
    curr_adj_vertex: Vertex[T] = None
    for adj_vertex in filter(lambda v: v.data not in visited, vertex.adjacent_vertices):
        curr_adj_vertex = adj_vertex
        adj_vertex_rank: int = 0
        for _adj_vertex in filter(lambda v: v.data not in visited, adj_vertex.adjacent_vertices):
            if _adj_vertex.data not in visited:
                adj_vertex_rank += 1
        print(adj_vertex, adj_vertex_rank)
        if adj_vertex_rank > 0 and adj_vertex_rank < min_rank:
            min_rank = adj_vertex_rank
            vertex_with_min_rank = adj_vertex

    if vertex_with_min_rank is None:
        min_rank = 0
        vertex_with_min_rank = curr_adj_vertex
    print(vertex, 'min: (vertex, rank)', vertex_with_min_rank, min_rank, '\n')

    return min_rank, vertex_with_min_rank

def get_adjacent_vertex_with_min_rank_via_Ira_Pohl(vertex: Vertex[T], visited: Set[T]) -> Tuple[int, Vertex[T]]:
    min_rank: int = sys.maxsize
    rank_vertex_mapping: Dict[int, List[Vertex[T]]] = defaultdict(list)
    for adj_vertex in filter(lambda v: v.data not in visited, vertex.adjacent_vertices):
        rank = get_vertex_rank(adj_vertex, visited)
        rank_vertex_mapping[rank].append(adj_vertex)
        if 0 < rank < min_rank:
            min_rank = rank
    vertices_with_min_rank: List[Vertex[T]] = rank_vertex_mapping[min_rank]
    if len(vertices_with_min_rank) == 0:
        vertices_with_rank_zero: List[Vertex[T]] = rank_vertex_mapping[0]
        if len(vertices_with_rank_zero) > 0:
            return 0, vertices_with_rank_zero[0]
    elif len(vertices_with_min_rank) == 1:
        return min_rank, vertices_with_min_rank[0]
    else:
        # Tie between multiple adjacent vertices with same min_rank, using Ira Pohl's algo.
        print('tie between vertices(with min_rank {}):'.format(min_rank), vertices_with_min_rank)
        _vertex: Vertex[T] = vertices_with_min_rank[0]
        _min_rank: int = sys.maxsize
        _rank_vertex_mapping: Dict[int, List[Vertex[T]]] = defaultdict(list)
        for tie_vertex in vertices_with_min_rank:
            visited_copy = copy.copy(visited)
            visited_copy.add(tie_vertex)
            _rank: int = get_vertex_rank(tie_vertex, visited_copy)
            _rank_vertex_mapping[_rank].append(tie_vertex)
            if 0 < _rank < _min_rank:
                _min_rank = _rank
                _vertex = tie_vertex

        print('After tie', 'vertices: ', [v for v in _rank_vertex_mapping[_min_rank]], 'with min_rank:', _min_rank)
        return min_rank, _vertex
    return -1, None


def get_vertex_rank(vertex: Vertex[T], visited: Set[T], log: bool = False) -> int:
    accessible_vertices: List[Vertex[T]] = list(filter(lambda v: v.data not in visited, vertex.adjacent_vertices))
    if log: print(accessible_vertices)
    return len(accessible_vertices)


# https://github.com/mak-aravind/PieceTour
# https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
# https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/
def warnsdoffs_algo(graph: Graph[T], rows:int = 4, cols:int = 4) -> List[List[int]]:
    chess: List[List[int]] = empty_2d_array(rows, cols, fill_default=-999)
    visited: Set[str] = set()
    step = 1

    curr_vertex = graph.vertices[0][1]
    # data_vertex_mapping: Dict[T, Vertex[T]] = {data: vertex for (data, vertex) in graph.vertices}
    # curr_vertex = data_vertex_mapping['4,9']

    indices: List[T] = curr_vertex.data.split(',')
    chess[int(indices[0])][int(indices[1])] = step

    while curr_vertex.data not in visited:
        visited.add(curr_vertex.data)
        rank, curr_vertex = get_adjacent_vertex_with_min_rank_via_Ira_Pohl(curr_vertex, visited)
        if curr_vertex is None:
            break
        step += 1
        indices: List[T] = curr_vertex.data.split(',')
        chess[int(indices[0])][int(indices[1])] = step

        # os.system(clear_screen)
        # print("This Move: [", graph_node.row, ",", graph_node.col, "]. Next Move: ", next_move, "Min Moves from next: ", min_no_moves)
        display(chess)
        import time
        time.sleep(.1)
        display(chess)
    return chess

def display(chess):
    print("")
    for row in chess:
        row_vals = []
        for cell in row:
            row_vals.append(cell)
        print(row_vals)

if __name__ == '__main__':
    rows: int = 8
    cols: int = 8
    graph: Graph[str] = build_graph(rows=rows, cols=cols)
    print(graph)
    print(graph.vertices)

    chess: List[List[int]] = warnsdoffs_algo(graph, rows=rows, cols=cols)
    print("\nResult: ")
    for c in chess:
        print(c)
    # print(chess)
#    0   1   2   3   4   5   6   7   8   9
# 0 [91, 25, 7,  92, 24, 6,  51, 16, 5,  32]
# 1 [61, 28, 89, 64, 29, 18, 3,  30, 19, 2]
# 2 [8,  95, 86, 26, 96, 85, 23, 33, 50, 15]
# 3 [90, 65, 62, 93, 88, 63, 52, 17, 4,  31]
# 4 [60, 27, 97, 76, 69, 34, 81, 70, 20, 1]
# 5 [9,  94, 87, 66, 99, 84, 22, 38, 49, 14]
# 6 [45, 77, 57, 54, 80, 75, 53, 35, 74, 40]
# 7 [59, 67, 98, 83, 68, -1, 82, 71, 21, 37]
# 8 [10, 55, 46, 11, 56, 47, 12, 39, 48, 13]
# 9 [44, 78, 58, 43, 79, 72, 42, 36, 73, 41]