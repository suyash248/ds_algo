from Tree.commons import Node, print_tree

def build_bst(arr, start, end):
    if start > end:
        return None
    mid = (start + end)/2
    root = Node(arr[mid])
    root.left = build_bst(arr, start, mid-1)
    root.right = build_bst(arr, mid+1, end)
    return root

# Driver program to test above function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    root = build_bst(arr, 0, len(arr)-1)
    print_tree(root)