from Tree.commons import Node, print_tree, is_leaf

# https://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/
# The idea is to do inorder traversal of the binary tree. While doing inorder traversal, keep track of the previously
# visited node in a variable say prev. For every visited node, make it next of prev and previous of this node as prev.


def binary_tree_to_DDL(root: Node):
    if root is not None:
        binary_tree_to_DDL(root.left)
        if binary_tree_to_DDL.prev is None:
            binary_tree_to_DDL.head = root
        else:
            root.left = binary_tree_to_DDL.prev
            binary_tree_to_DDL.prev.right = root
        binary_tree_to_DDL.prev = root
        binary_tree_to_DDL(root.right)

def print_DDL(head):
    temp = head
    while temp is not None:
        print(temp)
        temp = temp.right

if __name__ == '__main__':
    n10 = Node(10)
    n12 = Node(12)
    n25 = Node(25)
    n30 = Node(30)
    n15 = Node(15)
    n36 = Node(36)

    root = n10
    n10.left = n12
    n10.right = n15

    n12.left = n25
    n12.right = n30

    n15.left = n36

    print_tree(root)

    print("\nDDL\n")

    binary_tree_to_DDL.head = None
    binary_tree_to_DDL.prev = None
    binary_tree_to_DDL(root)

    print_DDL(binary_tree_to_DDL.head)