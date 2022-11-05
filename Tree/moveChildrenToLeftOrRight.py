from Tree.commons import insert, print_tree, is_leaf
import copy

""" Let us create following BST
        50
     /		\
    30		70
   /  \    /   \
  20  40  60 	80
"""
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

def move_children_left_v2(root):
    if root is None:
        return

    if root.right is not None:
        ltemp = root.left
        root.left = root.right
        root.right = None
        lmost = root.left
        while lmost.left is not None:
            lmost = lmost.left
        lmost.left = ltemp

    move_children_left_v2(root.left)
    move_children_left_v2(root.right)

def move_children_left_v3(root):
    if is_leaf(root):
        return

    if root.right is not None:
        ltemp = root.left
        root.left = root.right
        root.right = None
        lmost = root.left
        while lmost.left is not None:
            lmost = lmost.left
        lmost.left = ltemp

    move_children_left_v2(root.left)
    # move_children_left_v2(root.right) => root.right is set to None so there is no need to traverse right subtree

def swapChildren(r):
    if r is None:
        return
    right = r.right # copy.deepcopy(r.right)
    left = r.left # copy.deepcopy(r.left)

    r.left = right
    r.right = left

    swapChildren(r.left)
    swapChildren(r.right)

# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		\
        30		70
       /  \    /   \
      20  40  60 	80
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    r1 = copy.deepcopy(root)
    # move_children_left(r1)
    move_children_left_v2(r1)
    #move_children_right(r1)
    print_tree(r1)

    print("#################################")
    r2 = copy.deepcopy(root)
    swapChildren(r2)
    print_tree(r2)



# 50 : left->70 , right->NULL
# 70 : left->80 , right->NULL
# 80 : left->60 , right->NULL
# 60 : left->30 , right->NULL
# 30 : left->40 , right->NULL
# 40 : left->20 , right->NULL
# 20 : left->NULL , right->NULL