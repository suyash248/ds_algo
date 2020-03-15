__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from Array import empty_2d_array

class Graph(object):
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self._vertices = None
        self._sparse_matrix = None
        self._adjecency_list_v1 = dict()
        self._adjecency_list_v2 = []

    def sparse_matrix(self):
        self._vertices = list(map(lambda _: _.strip(), input("Enter vertices (comma-separated): ").split(',')))

        self._sparse_matrix = empty_2d_array(len(self._vertices), len(self._vertices), fill_default=0)

        for i in range(0, self.num_edges):
            print("Enter edge: {} ".format(i+1), end=', ')
            from_to = list(map(lambda _: _.strip(), input("from v1 to v2 (comma-separated, e.g. v1,v2): ").split(",")))
            from_vertex = from_to[0]
            to_vertex = from_to[1]
            print("{} --> {}".format(from_vertex, to_vertex))

            is_bi_directional_edge = True if input("Is this edge bi-directional ? (y/n): ").lower() == 'y' else False

            try:
                i_from_vertex = self._vertices.index(from_vertex)
                i_to_vertex = self._vertices.index(to_vertex)

                self._sparse_matrix[i_from_vertex][i_to_vertex] = 1
                if is_bi_directional_edge: self._sparse_matrix[i_to_vertex][i_from_vertex] = 1
            except ValueError as ve:
                print("Invalid vertices! Can't create an edge. Try again")
                self.num_edges += 1
        return self._sparse_matrix

    def print_sparse_matrix(self):
        if self._sparse_matrix is None or self._vertices is None:
            self.sparse_matrix()
        print('    ' + '  '.join(map(str, self._vertices)))
        print('   ' + '-- ' * len(self._vertices))
        for i in range(0, len(self._vertices)):
            print(self._vertices[i], end=' | ')
            print('  '.join(map(str, self._sparse_matrix[i])))

    def adjecency_list_v1(self):
        for i in range(0, self.num_edges):
            print("Enter edge: {} ".format(i + 1), end=', ')
            from_to = list(map(lambda _: _.strip(), input("from v1 to v2 (comma-separated, e.g. v1,v2): ").split(",")))
            from_vertex = from_to[0]
            to_vertex = from_to[1]
            print("{} --> {}".format(from_vertex, to_vertex))
            is_bi_directional_edge = True if input("Is this edge bi-directional ? (y/n): ").lower() == 'y' else False

            if from_vertex not in self._adjecency_list_v1:
                self._adjecency_list_v1[from_vertex] = set()
            self._adjecency_list_v1[from_vertex].add(to_vertex)
            if is_bi_directional_edge:
                if to_vertex not in self._adjecency_list_v1:
                    self._adjecency_list_v1[to_vertex] = set()
                self._adjecency_list_v1[to_vertex].add(from_vertex)

    def print_adjecency_list_v1(self):
        # a: c, b
        # b: e, a
        # e: d, b
        # d: c, e
        # c: a, d
        if len(self._adjecency_list_v1) == 0:
            self.adjecency_list_v1()

        for vertex, nodes in self._adjecency_list_v1.items():
            print('{vertex}: {nodes}'.format(vertex=vertex, nodes=', '.join(nodes)))

    # TODO
    def adjecency_list_v2(self):

        class Node(object):
            def __init__(self, data, next=None):
                self.data = data
                self.next = next

            def __hash__(self):
                return self.data.__hash_()

            def __eq__(self, other):
                return self.data == other.data

            def __str__(self):
                return "{}->{}".format(self.data, self.next.__str__() if self.next is not None else 'null')

            def __repr__(self):
                return self.__str__()

        def index(elt):
            for i, node in enumerate(self._adjecency_list_v2):
                if node.data == elt: return i
            return -1

        for i in range(0, self.num_edges):
            from_to = list(map(lambda _: _.strip(), input("from v1 to v2 (comma-separated, e.g. v1,v2): ").split(",")))
            from_vertex = from_to[0]
            to_vertex = from_to[1]
            print("{} --> {}".format(from_vertex, to_vertex))
            is_bi_directional_edge = True if input("Is this edge bi-directional ? (y/n): ").lower() == 'y' else False

            i_from_vertex = index(from_vertex)
            if i_from_vertex < 0:
                i_from_vertex = len(self._adjecency_list_v2)
                self._adjecency_list_v2.append(Node(from_vertex))

            temp = self._adjecency_list_v2[i_from_vertex]
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(to_vertex)

            if is_bi_directional_edge:
                i_to_vertex = index(to_vertex)
                if i_to_vertex < 0:
                    i_to_vertex = len(self._adjecency_list_v2)
                    self._adjecency_list_v2.append(Node(to_vertex))

                temp = self._adjecency_list_v2[i_to_vertex]
                while temp.next is not None:
                    temp = temp.next
                temp.next = Node(from_vertex)

        return self._adjecency_list_v2


if __name__ == '__main__':
    # a -- b
    # |      \
    # |       e
    # |      /
    # c -- d
    num_edges = int(input("Enter number of edges: "))
    graph = Graph(num_edges)

    # Sparse matrix
    #     a  b  c  d  e
    #    -- -- -- -- --
    # a | 0  1  1  0  0
    # b | 1  0  0  0  1
    # c | 1  0  0  1  0
    # d | 0  0  1  0  1
    # e | 0  1  0  1  0
    graph.sparse_matrix()
    graph.print_sparse_matrix()

    # Adjecency list using dict
    # a: b, c
    # b: a, e
    # e: d, b
    # d: c, e
    # c: a, d
    graph.adjecency_list_v1()
    graph.print_adjecency_list_v1()

    # Adjecency list using list
    # [a->b->c->null, b->a->e->null, e->b->d->null, d->e->c->null, c->d->a->null]
    adjecency_list = graph.adjecency_list_v2()
    print(adjecency_list)