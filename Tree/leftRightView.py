from commons.commons import insert

def left_view_v1(root, hd=0):
    if root is None:
        return

    if left_view_v1.hm.get(hd) is None:
        left_view_v1.hm[hd] = root.key

    left_view_v1(root.left, hd+1)
    left_view_v1(root.right, hd+1)


def right_view_v1(root, hd=0):
    if root is None:
        return

    right_view_v1.hm[hd] = root.key
    right_view_v1(root.left, hd+1)
    right_view_v1(root.right, hd+1)

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

    print "\n ---- Left View: Using V1 ---- \n"
    left_view_v1.hm = {}
    left_view_v1(root)
    print left_view_v1.hm.values()

    print "\n ---- Right View: Using V1 ---- \n"
    right_view_v1.hm = {}
    right_view_v1(root)
    print right_view_v1.hm.values()