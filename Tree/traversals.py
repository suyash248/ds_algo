from commons.commons import insert, print_tree, is_leaf

def preorder(root):
    if root:
        print root.key,
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print root.key,
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.key,

def level_order(root):
    from Queue import Queue
    q = Queue()
    q.put(root)
    while not q.empty():
        popped_elt = q.get()
        print popped_elt.key,
        if popped_elt.left: q.put(popped_elt.left)
        if popped_elt.right: q.put(popped_elt.right)

# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		\
        30		 70
      /    \   / 	\
    20 	   40 60 	80
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print "In-Order is - ", inorder(root)
    print "Pre-Order is - ", preorder(root)
    print "Post-Order is - ", postorder(root)
    print "Level-Order is - ", level_order(root)