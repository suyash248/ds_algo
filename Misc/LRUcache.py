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
    __count__ = 0
    __head__ = __tail__ = None
    __hm__ = {}

    # Time complexity: O(1)
    def insert(self, elt):
        """
        Inserts `elt` at the end.
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
        return node

    # Time complexity: O(1)
    def delete(self, elt):
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
        return node

    # Time complexity: O(1)
    def search(self, elt):
        return self.__hm__.get(elt, None)

    # Time complexity: O(1)
    def size(self):
        return self.__count__

    # Time complexity: O(n)
    def print_tail_to_head(self):
        temp = self.__tail__
        while temp is not None:
            print temp.data,
            temp = temp.prev
        print ""

    # Time complexity: O(n)
    def print_head_to_tail(self):
        temp = self.__head__
        while temp is not None:
            print temp.data,
            temp = temp.next
        print ""

if __name__ == '__main__':
    cdll = CustomDLL()
    cdll.insert(1)
    cdll.insert(2)
    cdll.insert(3)
    cdll.insert(4)
    cdll.insert(5)

    cdll.print_tail_to_head()
    cdll.print_head_to_tail()
    print cdll.size()

    cdll.delete(2)
    cdll.print_tail_to_head()
    cdll.print_head_to_tail()
    print cdll.size()

    cdll.delete(1)
    cdll.print_tail_to_head()
    cdll.print_head_to_tail()
    print cdll.size()

    cdll.delete(5)
    cdll.print_tail_to_head()
    cdll.print_head_to_tail()
    print cdll.size()