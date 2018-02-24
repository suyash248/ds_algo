import sys
from commons.commons import insert, is_leaf
from Array import MAX, MIN

def is_bst(root, min, max):
    if root is None:
        return True

    return (
            (root.key >= min and root.key < max)
            and is_bst(root.left, min, root.key-1)
            and is_bst(root.right, root.key + 1, max)
    )


def is_bst_v2(root):
    if root is None or is_leaf(root):
        return True

    left = root.left.key if root.left is not None else MIN
    right = root.right.key if root.right is not None else MAX

    return (
            (root.key >= left and root.key < right)
            and is_bst_v2(root.left)
            and is_bst_v2(root.right)
    )

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
    root1 = None
    root1 = insert(root1, 50)
    insert(root1, 30)
    insert(root1, 20)
    insert(root1, 15)
    insert(root1, 25)
    insert(root1, 40)
    insert(root1, 70)
    insert(root1, 60)
    insert(root1, 80)

    from commons.commons import Node
    root2 = Node(
        1,
        left=Node(
            2,
            left=Node(
                50
            )
        ),
        right=Node(
            3,
            left=Node(
                4
            ),
            right=Node(
                5,
                left=Node(
                    6
                )
            )
        )
    )

    print "\n ---------- USING V1 ---------- \n"

    b1 = is_bst(root1, MIN, MAX)
    b2 = is_bst(root2, MIN, MAX)
    print "Tree-1 is " + ("BST" if b1 else "Not BST")
    print "Tree-2 is " + ("BST" if b2 else "Not BST")

    print "\n ---------- USING V2 ---------- \n"

    b1 = is_bst_v2(root1)
    b2 = is_bst_v2(root2)
    print "Tree-1 is " + ("BST" if b1 else "Not BST")
    print "Tree-2 is " + ("BST" if b2 else "Not BST")
