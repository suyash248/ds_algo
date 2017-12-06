from commons.commons import insert, print_tree, is_leaf

def move_children_right(root):
    if root is None:
        return
    move_children_right(root.left)
    move_children_right(root.right)

    if root.left is not None:
        rtemp = root.right
        root.right = root.left
        root.left = None
        rmost = root.right
        while rmost.right is not None:
            rmost = rmost.right
        rmost.right = rtemp

def move_children_left(root):
    if root is None:
        return
    move_children_left(root.left)
    move_children_left(root.right)

    if root.right is not None:
        ltemp = root.left
        root.left = root.right
        root.right = None
        lmost = root.left
        while lmost.left is not None:
            lmost = lmost.left
        lmost.left = ltemp

# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		\
        30		70
        / 	\   / 	\
        20 	40	60 	80
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    move_children_left(root)
    #move_children_right(root)
    print_tree(root)