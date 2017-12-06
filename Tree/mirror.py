from commons.commons import insert, print_tree
from copy import deepcopy

def convert_to_mirror(root):
    if root is None:
        return None

    lsubtree = convert_to_mirror(root.left)
    rsubtree = convert_to_mirror(root.right)

    root.left = rsubtree
    root.right = lsubtree

    return root

def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
        return False
    return (root1.key == root2.key) and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)

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

    print "\n----- Tree -----\n"
    print_tree(root)

    print "\n----- Mirror -----\n"
    mirror_root = deepcopy(root)
    convert_to_mirror(mirror_root)
    print_tree(mirror_root)

    print "\n---- Are mirror ? ----\n", is_mirror(root, mirror_root)