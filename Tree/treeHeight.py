from commons.commons import insert, print_tree, is_leaf

def calculate_height(root):
    if root == None:
        return 0
    return max(calculate_height(root.left), calculate_height(root.right)) + 1

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

    h = calculate_height(root)
    print "Height is {height}".format(height=h)