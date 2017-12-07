from commons.commons import Node, print_tree, is_leaf

# fs(50) - 50, fs(30)
#					fs(30) - 80, fs(20)
#									fs(20) - 100
def children_sum(root):
    if root is None:
        return False
    if is_leaf(root):
        return True

    lkey = root.left.key if root.left is not None else 0
    rkey = root.right.key if root.right is not None else 0

    if root.key != (lkey + rkey):
        return False
    return children_sum(root.left) and children_sum(root.right)


# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following binary tree
            55
         /		\
        20		35
       /  \    /  \
      5   15  25  10
    """
    root = None
    root = Node(55)
    node20 = Node(20)
    node35 = Node(35)
    node5 = Node(5)
    node15 = Node(15)
    node25 = Node(25)
    node10 = Node(10)

    root.left = node20
    root.right = node35

    node20.left = node5
    node20.right = node15

    node35.left = node25
    node35.right = node10

    print "Is binary tree following children-sum property?", children_sum(root)