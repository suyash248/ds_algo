# A tree node
class Node:
    # Constructor to create a new node
    def __init__(self, key, left=None, right=None, hd=None):
        self.key = key
        self.left = left
        self.right = right
        self.hd = hd


def insert(node, key):
    """
    A utility function to insert a new node in with given key in BST
    :param node:
    :param key:
    :return:
    """
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def is_leaf(node):
    return node and node.left is None and node.right is None

def print_tree(root):
    if root is None:
        return
    else:
        left = str(root.left.key) if root.left is not None else "NULL"
        right = str(root.right.key) if root.right is not None else "NULL"
        print (str(root.key) + " : left->{left} , right->{right}".format(left=left, right=right))
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    root = Node(
            1,
            left=Node(
                2,
                left=Node(
                    50
                )
            ),
            right=Node(
                3,
                left=Node(
                    4
                ),
                right=Node(
                    5,
                    left=Node(
                        6
                    )
                )
            )
         )
    print_tree(root)