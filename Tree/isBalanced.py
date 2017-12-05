from commons.commons import insert, is_leaf
from treeHeight import calculate_height

def is_balanced(root):
    if root == None:
        return True

    lh = calculate_height(root.left)
    rh = calculate_height(root.right)

    return abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right)


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
    insert(root, 30);
    insert(root, 20);
    insert(root, 15);
    insert(root, 25);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    # insert(root, 10);
    # insert(root, 41);
    # insert(root, 90);

    b = is_balanced(root)
    print b
    #print "Balanced" if b else "Not balanced"