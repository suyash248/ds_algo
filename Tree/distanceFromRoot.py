from commons.commons import insert, print_tree, is_leaf

def distance_from_root(root, key, distance=0):
    if root == None:
        return 0
    distance += 1

    if root.key == key:
        return distance
    else:
        ld = distance_from_root(root.left, key, distance)
        rd = distance_from_root(root.right, key, distance)
    return ld if ld > 0 else rd

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

    key = 60
    distance = distance_from_root(root, key)
    print "Distance from root({root}) to {key} is {distance}".format(root=root.key, key=key, distance=distance)