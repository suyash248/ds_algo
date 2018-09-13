from Tree.commons import Node, print_tree, insert
from Tree.buildBSTFromSortedArray import build_bst

def balance_tree(root):
    inorder_arr = []
    inorder(root, inorder_arr)
    return build_bst(inorder_arr, 0, len(inorder_arr)-1)

def inorder(root, inorder_arr):
    if root is not None:
        inorder(root.left, inorder_arr)
        inorder_arr.append(root.key)
        inorder(root.right, inorder_arr)

# Driver program to test above function
if __name__ == "__main__":
    """ Unbalanced BST
                50
               /  \
              30  70
        	       \
       	            80
       	             \
       	              90
     
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 70)
    insert(root, 80)
    insert(root, 90)

    print ("\n ---- Unbalanced BST ----\n")
    print_tree(root)

    print ("\n ---- Balanced BST ----\n")

    balanced_root = balance_tree(root)
    print_tree(balanced_root)

    """
        Balanced BST ->
        
        70
      /    \
     30     80
       \     \
        50    90
    """
