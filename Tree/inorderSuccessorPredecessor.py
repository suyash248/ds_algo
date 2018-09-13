from Tree.commons import insert, print_tree, is_leaf

# This function finds predecessor and successor of key in BST
# It sets pre and suc as predecessor and successor respectively
"""
1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most 
        child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child 
        of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root
        search recursively into left subtree
    else
        set the predecessor as root
        search recursively into right subtree
"""
def findPreSuc(root, key):
    # Base Case
    if root is None:
        return

    # If key is present at root
    if root.key == key:

        # the maximum value in left subtree is predecessor
        if root.left is not None:
            tmp = root.left
            while (tmp.right):
                tmp = tmp.right
            findPreSuc.pre = tmp

        # the minimum value in right subtree is successor
        if root.right is not None:
            tmp = root.right
            while (tmp.left):
                tmp = tmp.left
            findPreSuc.suc = tmp

        return

    # If key is smaller than root's key, go to left subtree
    if root.key > key:
        findPreSuc.suc = root
        findPreSuc(root.left, key)

    else:  # go to right subtree
        findPreSuc.pre = root
        findPreSuc(root.right, key)

# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		\
        30		70
       /  \    /   \
     20   40  60 	80
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    findPreSuc.pre = findPreSuc.suc = None
    key = 30
    findPreSuc(root, key)
    print ("Predecessor of {key} is {pre}, and Successor of {key} is {suc}".format(key=key,
          pre=findPreSuc.pre.key,
          suc=findPreSuc.suc.key))