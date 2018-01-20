import Queue
from collections import OrderedDict
from commons.commons import insert, Node, print_tree


max_level = -1
def left_view(root, curr_level=0):
    global max_level
    if root is None:
        return

    if max_level < curr_level:
        print root.key,
        max_level = curr_level

    # Recur for left subtree first, then right subtree
    left_view(root.left, curr_level + 1)
    left_view(root.right, curr_level + 1)


def right_view(root, curr_level=0):
    global max_level
    if root is None:
        return

    if max_level < curr_level:
        print root.key,
        max_level = curr_level

    # Recur for right subtree first, then left subtree
    right_view(root.right, curr_level + 1)
    right_view(root.left, curr_level + 1)


def top_view(root):
    hm = {}
    q = Queue.Queue()
    root.hd = 0
    q.put(root)
    hm[0] = root.key

    while not q.empty():
        popped_node = q.get()

        if popped_node.left is not None:
            popped_node.left.hd = popped_node.hd - 1
            if not hm.has_key(popped_node.left.hd):
                hm[popped_node.left.hd] = popped_node.left.key
            q.put(popped_node.left)

        if popped_node.right is not None:
            popped_node.right.hd = popped_node.hd + 1
            if not hm.has_key(popped_node.right.hd):
                hm[popped_node.right.hd] = popped_node.right.key
            q.put(popped_node.right)

    hm = OrderedDict(sorted(hm.items()))
    return hm.values()


def bottom_view(root):
    hm = {}
    q = Queue.Queue()
    root.hd = 0
    q.put(root)
    hm[0] = root.key

    while not q.empty():
        popped_node = q.get()

        if popped_node.left is not None:
            popped_node.left.hd = popped_node.hd - 1
            hm[popped_node.left.hd] = popped_node.left.key
            q.put(popped_node.left)

        if popped_node.right is not None:
            popped_node.right.hd = popped_node.hd + 1
            hm[popped_node.right.hd] = popped_node.right.key
            q.put(popped_node.right)

    hm = OrderedDict(sorted(hm.items()))
    return hm.values()

# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		 \
        30		  70
       /  \     / 	 \
      20   40  60 	  80
     /   \
    15   25
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 15)
    insert(root, 25)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print "\n ---- Left View ---- \n"
    left_view(root, 0)
    max_level = -1
    print "\n"

    print "\n ---- Right View ---- \n"
    right_view(root, 0)
    max_level = -1
    print "\n"

    print "\n ---- Top View ---- \n"
    top_view_nodes = top_view(root)
    print top_view_nodes

    print "\n ---- Bottom View ---- \n"
    bottom_view_nodes = bottom_view(root)
    print bottom_view_nodes


# root2 = Node(
#         20,
#         left=Node(
#             8,
#             left=Node(
#                 5
#             ),
#             right=Node(
#                 3,
#                 left=Node(
#                     10
#                 ),
#                 right=Node(
#                     14
#                 )
#             )
#         ),
#         right=Node(
#             22,
#             left=Node(
#                 4
#             ),
#             right=Node(
#                 25
#             )
#         )
#     )