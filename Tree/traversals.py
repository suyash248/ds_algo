from commons.commons import insert, print_tree, is_leaf

def preorder(root):
    if root:
        print(root.key, end=',')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=',')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=',')

def level_order(root):
    from queue import Queue
    q = Queue()
    q.put(root)
    while not q.empty():
        popped_elt = q.get()
        print(popped_elt.key, end=',')
        if popped_elt.left: q.put(popped_elt.left)
        if popped_elt.right: q.put(popped_elt.right)

def spiral(root):
    stack1 = [root]
    stack2 = []

    while len(stack1) or len(stack2):
        while len(stack1):
            popped_node = stack1.pop()
            print(popped_node.key, end=',')
            # left first then right
            if popped_node.left is not None: stack2.append(popped_node.left)
            if popped_node.right is not None: stack2.append(popped_node.right)

        while len(stack2):
            popped_node = stack2.pop()
            print(popped_node.key, end=',')
            # right first then left
            if popped_node.right is not None: stack1.append(popped_node.right)
            if popped_node.left is not None: stack1.append(popped_node.left)

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

    print("In-Order is - ")
    inorder(root)
    print("\nPre-Order is - ")
    preorder(root)
    print("\nPost-Order is - ")
    postorder(root)
    print("\nLevel-Order is - ")
    level_order(root)
    print("\nSprial(zig-zag)-Order is - ")
    spiral(root)