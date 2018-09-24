from Tree.commons import insert, Node, print_tree
from queue import Queue

def diagonals_sum_recursive(root, d=0):
    if root is None:
        return

    if d in diagonals_sum_recursive.hm:
        diagonals_sum_recursive.hm[d].append(root.key)
    else:
        diagonals_sum_recursive.hm[d] = [root.key]

    diagonals_sum_recursive(root.left, d + 1)
    diagonals_sum_recursive(root.right, d)

# https://www.youtube.com/watch?v=I3BC8nEKYm8
# https://www.geeksforgeeks.org/diagonal-sum-binary-tree/
def diagonals_sum_iterative(root):
    q = Queue()
    q.put(root)
    q.put(None)
    sum = 0
    while not q.empty():
        pnode = q.get()
        if pnode is None:
            # A delimiter `None` is used to mark the starting of next diagonal.
            # Diagonal is complete, print sum.
            print(sum)
            sum = 0
            q.put(None)
            pnode = q.get()

        while pnode is not None:
            sum += pnode.key
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

    print("\n------------------ Using recursive approach ------------------\n")

    diagonals_sum_recursive.hm = {}
    diagonals_sum_recursive(root)
    for k,v in diagonals_sum_recursive.hm.items():
        print(sum(v))

    print("\n------------------ Using iterative approach ------------------\n")

    diagonals_sum_iterative(root)