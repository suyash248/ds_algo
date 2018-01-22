from commons.commons import insert, Node, print_tree
from Queue import Queue

# https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
def diagonals_recursive(root, d=0):
    if root is None:
        return

    if d in diagonals_recursive.hm:
        diagonals_recursive.hm[d].append(root.key)
    else:
        diagonals_recursive.hm[d] = [root.key]

    diagonals_recursive(root.left, d + 1)
    diagonals_recursive(root.right, d)

# https://www.youtube.com/watch?v=e9ZGxH1y_PE
def diagonals_iterative(root):
    q = Queue()
    q.put(None)
    q.put(root)
    while not q.empty():
        pnode = q.get()
        if pnode is None:
            # Diagonal is complete.
            print ""
            q.put(None)
            pnode = q.get()
            pass
        while pnode is not None:
            print pnode.key,
            if pnode.left is not None:
                q.put(pnode.left)
            pnode = pnode.right


if __name__ == '__main__':
    """
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

    print "\n------------------ Using recursive approach ------------------\n"

    diagonals_recursive.hm = {}
    diagonals_recursive(root)
    print diagonals_recursive.hm

    print "\n------------------ Using iterative approach ------------------\n"

    diagonals_iterative(root)