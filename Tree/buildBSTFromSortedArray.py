# Python program to find predecessor and successor in a BST

# A BST node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_bst(arr, start, end):
    if start > end:
        return None
    mid = (start + end)/2
    root = Node(arr[mid])
    root.left = build_bst(arr, start, mid-1)
    root.right = build_bst(arr, mid+1, end)
    return root

def print_tree(root):
    if root is None:
        return
    else:
        left = str(root.left.key) if root.left is not None else "NULL"
        right = str(root.right.key) if root.right is not None else "NULL"
        print str(root.key) + " : left->{left} , right->{right}".format(left=left, right=right)
    print_tree(root.left)
    print_tree(root.right)

# Driver program to test above function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    root = build_bst(arr, 0, len(arr)-1)
    print_tree(root)