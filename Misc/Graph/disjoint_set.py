from __future__ import annotations

__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

from typing import TypeVar, Generic, Dict

T = TypeVar('T')

# References:
# https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/DisjointSet.java
# https://www.youtube.com/watch?v=ID00PMy0-vE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
class DisjointNode(Generic[T]):
    def __init__(self, data: T, parent: DisjointNode[T] = None, rank: int = 0):
        self.data = data
        self.rank = rank
        self.parent = parent

    def __str__(self):
        parent_data = None
        if self.parent: parent_data = self.parent.data
        return "data: {}| rank: {}| parent: {}".format(self.data, self.rank, parent_data)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.data.__hash__()

    def __eq__(self, other):
        if other is not None: return self.data == other.data
        return False

# Space complexity: O(n)
# Space complexity: O(m), where n is number or elements, m is number of operations.
class DisjointSet(Generic[T]):
    def __init__(self):
        self.__data_node_mapping__: Dict[T, DisjointNode[T]] = dict()

    def make_set(self, data: T):
        """
        Creates a set with only one node(having data as `data`) with rank 0 and it's parent will be this node itself.

        :param data:
        """
        node: DisjointNode[T] = self.__data_node_mapping__.get(data)
        if node is None:
            node = DisjointNode(data)
            node.parent = node
            self.__data_node_mapping__[data] = node

    def find_set(self, data: T) -> DisjointNode[T]:
        """
        Finds set(representative node) and also performs path compression to make subsequent find_set calls faster
        by avoiding skewed tree(By attaching all the descendants to root node directly).

        :param data: target data node.
        :return: Representative node of the set where the node(corresponding to data) belongs to.
        """
        def __find_set__(node: DisjointNode[T]) -> DisjointNode[T]:
            if node.parent == node:
                return node.parent
            node.parent = __find_set__(node.parent) # Path compression: After path compression, height of tree will be reduced to 1.
            return node.parent

        return __find_set__(self.__data_node_mapping__[data])

    def union(self, data1: T, data2: T) -> bool:
        """
        Combines two sets(set containing the node corresponding to `data1` and the set containing the node
        correspondingto `data2`.

        :param data1:
        :param data2:

        :return: `True`, if both data1 and data2 belong to different sets, `False` otherwise.
        """
        parent1: DisjointNode[T] = self.find_set(data1)
        parent2: DisjointNode[T] = self.find_set(data2)

        if parent1.data == parent2.data:
            return False

        # node with higher rank will be the parent of other node.
        if parent1.rank > parent2.rank:
            parent2.parent = parent1
        elif parent2.rank > parent1.rank:
            parent1.parent = parent2
        else:
            # If rank of both nodes is same, make any one of them as parent of another and increment parent's rank.
            parent1.rank += 1
            parent2.parent = parent1
        return True

    def __str__(self):
        a = []
        for data, node in self.__data_node_mapping__.items():
            a.append(node.__str__())
        return '\n'.join(a)

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    ds: DisjointSet[int] = DisjointSet()
    ds.make_set(1)
    ds.make_set(2)
    ds.make_set(3)
    ds.make_set(4)
    ds.make_set(5)
    ds.make_set(6)
    ds.make_set(7)

    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(5, 6)
    ds.union(3, 7)

    print(ds.find_set(1))
    print(ds.find_set(2))
    print(ds.find_set(3))
    print(ds.find_set(4))
    print(ds.find_set(5))
    print(ds.find_set(6))
    print(ds.find_set(7))

    print('\n')
    print(ds)
