# Please visit https://www.youtube.com/watch?v=LTNdPuP0P6U for more information about designing LRU cache.

from copy import deepcopy

class Node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        prev_data = self.prev.data if self.prev is not None else None
        next_data = self.next.data if self.next is not None else None
        return "{prev_data} <- {data} -> {next_data}".format(prev_data=prev_data, next_data=next_data, data=self.data)

class CustomDLL(object):
    """
    This class represents a custom DLL wherein insert, delete, search operations can be performed in O(1) i.e. constant
    time. Elements are also copied to `hashtable(dict)` which helps in searching the element(s) in constant time.
    Each entry in `hashtable(dict)` stores  `element_data: Node() reference` key-value pair.

        * Insert - Element is inserted at the tail/end. Also copy the element to `hashtable(dict)`.
        * Search - Element is searched in `hashtable(dict)` and corresponding `Node` reference is returned.
        * Delete - Element is searched in `hashtable(dict)` and deleted from `hashtable(dict)` as well as from DLL.

    | Time complexity: O(1)
    | Space complexity: O(n)
    """
    __count__ = 0
    __head__ = __tail__ = None
    __hm__ = {}

    # Time complexity: O(1)
    def insert(self, elt):
        """
        Inserts `elt` at the end(at `tail`). Also updates underlying hashtable `hm`.
        :param elt:
        :return:
        """
        node = Node(data=elt, prev=self.__tail__)

        # First node
        if self.__count__ == 0:
            self.__head__ = node

        elif self.__tail__ is not None:
            self.__tail__.next = node

        self.__tail__ = node

        self.__count__ += 1
        self.__hm__[elt] = node
        return deepcopy(node)

    # Time complexity: O(1)
    def delete(self, elt):
        """
        Finds and deletes node representing `elt`. Also updates underlying hashtable `hm`.
        :param elt:
        :return:
        """
        node = self.search(elt)
        if node is None:
            return None

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.__head__ = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.__tail__ = node.prev

        self.__hm__.pop(elt)
        self.__count__ -= 1
        return deepcopy(node)

    # Time complexity: O(1)
    def search(self, elt):
        # IMPORTANT! - Return exact reference of node, do NOT use deepcopy here
        # otherwise we won't be able to change links(prev, next) on original node while deletion.
        return self.__hm__.get(elt, None)

    def head(self):
        """
        :return: Copy of node at the head.
        """
        return deepcopy(self.__head__)

    def tail(self):
        """
        :return: Copy of node at the tail.
        """
        return deepcopy(self.__tail__)

    # Time complexity: O(1)
    def size(self):
        """
        :return: Number of nodes in CDLL.
        """
        return self.__count__

    # Time complexity: O(n)
    def print_tail_to_head(self):
        temp = self.__tail__
        while temp is not None:
            print(temp.data, end=',')
            temp = temp.prev
        print("")

    # Time complexity: O(n)
    def print_head_to_tail(self):
        temp = self.__head__
        while temp is not None:
            print(temp.data, end=',')
            temp = temp.next
        print("")

class Result(object):
    HIT = "HIT"
    MISS = "MISS"
    def __init__(self, hitOrMiss, data=None):
        self.hitOrMiss = hitOrMiss
        self.data = data

    def __str__(self):
        return self.hitOrMiss + " - " + str(self.data)

class LRUcache(object):
    """
    `CustomDLL` i.e. cdll will be used to represent LRU cache in following way -
        - `Most Recently Used` element will be at the end of `cdll` (i.e. at the `tail`) -> Newest entry in cache.
        - `Least Recently Used` element will be at the start of `cdll` (i.e. at the `head`) -> Oldest entry in cache.
    """
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.__cdll__ = CustomDLL()

    def put(self, elt):
        """
        if elt is in cache/cdll:
            update it's position as follows -
                a. delete elt from cache/cdll
                b. insert elt in cache/cdll(at tail)
        else:
            if cache/cdll is full:
                remove oldest entry(present at head) from cache/cdll
            insert elt in cache/cdll(at tail)
        :param elt:
        :return: `Result` (Hit/Miss)
        """
        node_entry = self.__cdll__.search(elt)
        if node_entry is not None:
            self.__cdll__.delete(elt)
            self.__cdll__.insert(elt)
            return Result(Result.HIT, node_entry.data)
        else:
            if self.full():
                oldest_node_entry = self.__cdll__.head()
                self.__cdll__.delete(oldest_node_entry.data)
            self.__cdll__.insert(elt)
        return Result(Result.MISS)

    def get(self, elt):
        """
        if elt is in cache/cdll:
            update it's position as follows -
                a. delete elt from cache/cdll
                b. insert elt in cache/cdll(at tail)
        :param elt:
        :return: `Result` (Hit/Miss)
        """
        node_entry = self.__cdll__.search(elt)
        if node_entry is not None:
            self.__cdll__.delete(elt)
            self.__cdll__.insert(elt)
            return Result(Result.HIT, node_entry.data)
        return Result(Result.MISS)

    def size(self):
        """
        size of cache/cdll.
        :return:
        """
        return self.__cdll__.size()

    def full(self):
        return self.size() == self.capacity

    def print_cache(self):
        """
        Prints LRU cache from `most recently used` element to `least recently used` element.
        :return:
        """
        self.__cdll__.print_tail_to_head()

    def __len__(self):
        return self.size()

def test_cdll():
    cdll = CustomDLL()
    cdll.insert(1)
    cdll.insert(2)
    cdll.insert(3)
    cdll.insert(4)
    cdll.insert(5)

    #cdll.print_tail_to_head()
    cdll.print_head_to_tail()
    print("Size - ", cdll.size())

    del_res = cdll.delete(2)
    print("Deleted", del_res)
    cdll.print_head_to_tail()
    # print "Size - ", cdll.size()
    # print "HEAD", cdll.head()
    # print "TAIL", cdll.tail()

    # cdll.delete(1)
    # cdll.print_tail_to_head()
    # cdll.print_head_to_tail()
    # print cdll.size()
    #
    # cdll.delete(5)
    # cdll.print_tail_to_head()
    # cdll.print_head_to_tail()
    # print cdll.size()

if __name__ == '__main__':
    #test_cdll()
    capacity = input("Enter the capacity of LRU cache - ")
    lru = LRUcache(capacity=capacity)

    choices = "\n1. Put\n2. Get\n3. Size\n4. Is Full?\n5. Print cache\n6. Exit\n"
    while True:
        print(choices)
        choice = input("Please enter your choice - ")

        if choice == 1:
            elt = input("Please enter element to be inserted - ")
            res = lru.put(elt)
            print(res)
        elif choice == 2:
            elt = input("Please enter element to be searched - ")
            res = lru.get(elt)
            print(res)
        elif choice == 3:
            print("Size -",lru.size())
        elif choice == 4:
            print("LRU cache is full -", lru.full())
        elif choice == 5:
            print("Cache - ")
            lru.print_cache()
        elif choice == 6:
            break
        else:
            print("Invalid choice")
            continue

