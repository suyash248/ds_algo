from commons.commons import insert

def print_K_distant_v1(root, k):
    if root is None:
        return
    if k == 0:
        print root.key,
    else:
        print_K_distant_v1(root.left, k - 1)
        print_K_distant_v1(root.right, k - 1)

def print_K_distant_v2(root, k, distance=-1):
    if root is None:
        return
    distance += 1
    if distance == k:
        print root.key,
    print_K_distant_v2(root.left, k, distance)
    print_K_distant_v2(root.right, k, distance)

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

    k = 2

    print "\n----- Using V1 -----\n"
    print "Nodes at distance {distance} from root({root} are - )".format(distance=k, root=root.key)
    print_K_distant_v1(root, k)

    print "\n----- Using V1 -----\n"
    print "Nodes at distance {distance} from root({root} are - )".format(distance=k, root=root.key)
    print_K_distant_v2(root, k)
