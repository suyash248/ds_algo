from commons.commons import insert, is_leaf
from treeHeight import calculate_height

# O(n^2)
def is_balanced_v1(root):
    if root == None:
        return True

    lh = calculate_height(root.left)
    rh = calculate_height(root.right)

    return abs(lh - rh) <= 1 and is_balanced_v1(root.left) and is_balanced_v1(root.right)

# Calculates height in same function call only, O(n)
def is_balanced_v2(root):
    if root == None:
        return 0, True

    lh, is_left_balanced = is_balanced_v2(root.left)
    rh, is_right_balanced = is_balanced_v2(root.right)

    h = max(lh, rh) + 1
    is_bal = abs(lh - rh) <= 1 and is_left_balanced and is_right_balanced
    return h, is_bal


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
    # insert(root, 10)
    # insert(root, 41)
    # insert(root, 90)

    print "\n---- Using V1 ----\n"
    b = is_balanced_v1(root)
    print "Tree is " + "balanced" if b else "Not balanced"

    print "\n---- Using V2 ----\n"
    h, b = is_balanced_v2(root)
    print "Height of tree is {height} and tree is".format(height=h) + " Balanced" if b else "Not balanced"

