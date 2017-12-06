from commons.commons import insert, print_tree, is_leaf
from treeHeight import calculate_height

# O(n^2)
def calculate_diameter_v1(root):
    if root == None:
        return 0

    lh = calculate_height(root.left)
    rh = calculate_height(root.right)

    diameter_via_height = lh + rh + 1

    ld = calculate_diameter_v1(root.left)
    rd = calculate_diameter_v1(root.right)

    diameter_via_left_right_subtree = ld + rd
    return max(diameter_via_height, diameter_via_left_right_subtree)

# O(n)
def calculate_diameter_v2(root):
    if root == None:
        return 0

    lh = calculate_diameter_v2(root.left)
    rh = calculate_diameter_v2(root.right)

    calculate_diameter_v2.d = max(calculate_diameter_v2.d, lh + rh + 1)
    return max(lh, rh) + 1


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

    print "\n----- Diameter via V1 -----\n"
    d = calculate_diameter_v1(root)
    print "Diameter is {diameter}".format(diameter=d)

    print "\n----- Diameter via V2 -----\n"
    calculate_diameter_v2.d = -1
    d = calculate_diameter_v2(root)
    print "Diameter is {diameter}".format(diameter=calculate_diameter_v2.d)