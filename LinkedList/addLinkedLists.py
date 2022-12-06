class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{} | next -> ".format(self.data, self.next.data if self.next else None)


"""
Algorithm -

In this problem, most significant node is first node and least significant digit is last node and we are not allowed to 
modify the lists. Recursion is used here to calculate sum from right to left.

Following are the steps.
1) Calculate sizes of given two linked lists.
2) If sizes are same, then calculate sum using recursion. Hold all nodes in recursion call stack till the rightmost node, 
    calculate sum of rightmost nodes and forward carry to left side.
3) If size is not same, then follow below steps:
    a) Calculate difference of sizes of two linked lists. Let the difference be diff
    b) Move diff nodes ahead in the bigger linked list. Now use step 2 to calculate sum of smaller list and 
        right sub-list (of same size) of larger list. Also, store the carry of this sum.
    c) Calculate sum of the carry (calculated in previous step) with the remaining left sub-list of larger list. 
        Nodes of this sum are added at the beginning of sum list obtained previous step.

References- https://www.geeksforgeeks.org/sum-of-two-linked-lists/
"""


class Adder(object):
    def __init__(self, head1, head2):
        self.head1 = head1
        self.head2 = head2
        self.result_head = None
        self.__carry__ = 0
        self.__sum__ = ""

    def __add_same_size_lists__(self, node1, node2):
        if node1 is None or node2 is None:
            return

        self.__add_same_size_lists__(node1.next, node2.next)
        cur_sum = self.__carry__ + node1.data + node2.data

        self.__carry__ = cur_sum / 10
        new_node = Node(cur_sum % 10, next=self.result_head)
        self.result_head = new_node

        self.__sum__ += str(new_node.data)

    def add(self):
        size1 = Adder.get_size(head1)
        size2 = Adder.get_size(head2)
        diff = abs(size1 - size2)

        if diff > 0:
            # Makes sure that first linked list(i.e. head1) is always larger one.
            if size1 < size2:
                self.head1, self.head2 = self.head2, self.head1

            sublist_head = self.head1
            while diff > 0:
                sublist_head = sublist_head.next
                diff -= 1

            self.__add_same_size_lists__(sublist_head, self.head2)

            # Add carry to left sublist of larger list.
            self.__propagate_carry__(self.head1, sublist_head)

        # If lists are of same size. i.e. diff = 0
        else:
            self.__add_same_size_lists__(self.head1, self.head2)

        if self.__carry__ != 0:
            new_node = Node(self.__carry__, next=self.result_head)
            self.result_head = new_node
            self.__sum__ += str(new_node.data)

        self.__sum__ = int(self.__sum__[::-1])
        return self.__sum__, self.result_head

    def __propagate_carry__(self, head, sublist_head):
        """
        This function is called after the smaller list is added to the bigger lists's sublist of same size.
        Once the right sublist is added, the carry must be added to the left side of larger list to get the
        final result.

        :param head:
        :param sublist_head:
        :return:
        """
        if sublist_head != head:
            self.__propagate_carry__(head.next, sublist_head)
            cur_sum = self.__carry__ + head.data

            self.__carry__ = cur_sum / 10
            new_node = Node(cur_sum % 10, next=self.result_head)
            self.result_head = new_node

            self.__sum__ += str(new_node.data)
            # temp = temp.next

    @classmethod
    def get_size(cls, head):
        size = 0
        cur = head
        while cur is not None:
            size += 1
            cur = cur.next
        return size

    @classmethod
    def print_list(cls, head):
        cur = head
        while cur is not None:
            print(str(cur.data) + "->")
            cur = cur.next
        print(None)


def create_linked_list(data=None):
    if data is None: return None
    head = prev = Node(data[0])
    for elt in data[1:]:
        cur = Node(elt)
        prev.next = cur
        prev = cur
    return head


# Input:
#   First List: 5->6->3         // represents number 563
#   Second List: 8->4->2        //  represents number 842
# Output
#   Resultant list: 1->4->0->5  // represents number 1405
if __name__ == '__main__':
    head1 = create_linked_list([2, 8, 9, 7])
    head2 = create_linked_list([1, 8])

    print("List-1: ")
    Adder.print_list(head1)
    print("List-2: ")
    Adder.print_list(head2)

    adder = Adder(head1, head2)
    result_sum, result_head = adder.add()

    print("Result list: ")
    Adder.print_list(result_head)

    print("Total sum: {}".format(result_sum))
