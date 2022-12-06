class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{} | next -> ".format(self.data, self.next.data if self.next else None)


"""
Algorithm -

Traverse both lists and generate the required numbers to be multiplied and then return the multiplied values of the two numbers.
Algorithm to generate the number from linked list representation:

1) Initialize a variable to zero
2) Start traversing the linked list
3) Add the value of first node to this variable
4) From the second node, multiply the variable by 10
   first and then add the value of the node to this 
   variable.
5) Repeat step 4 until we reach the last node of the list. 

References- https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists/
"""


class Multiplier(object):

    def __init__(self, head1, head2):
        self.head1 = head1
        self.head2 = head2

    def multiply(self):
        first = self.head1
        second = self.head2

        num1 = num2 = 0
        while first or second:
            if first:
                num1 = num1 * 10 + first.data
                first = first.next
            if second:
                num2 = num2 * 10 + second.data
                second = second.next

        return num1 * num2

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


def create_linked_list(data=[]):
    head = prev = Node(data[0])
    for elt in data[1:]:
        cur = Node(elt)
        prev.next = cur
        prev = cur
    return head


if __name__ == '__main__':
    head1 = create_linked_list([1, 0, 5])
    head2 = create_linked_list([1, 2])

    print("List-1: ")
    Multiplier.print_list(head1)
    print("List-2: ")
    Multiplier.print_list(head2)

    multiplier = Multiplier(head1, head2)
    result = multiplier.multiply()

    print("Result: {}".format(result))
