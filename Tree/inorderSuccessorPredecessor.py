# Python program to find predecessor and successor in a BST

# A BST node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# This fucntion finds predecessor and successor of key in BST
# It sets pre and suc as predecessor and successor respectively
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

# A utility function to insert a new node in with given key in BST
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def print_tree(root):
    if root is None:
        return
    else:
        left = str(root.left.key) if root.left is not None else "NULL"
        right = str(root.right.key) if root.right is not None else "NULL"
        print str(root.key) + " : left->{left} , right->{right}".format(left=left, right=right)
    print_tree(root.left)
    print_tree(root.right)
# Driver program to test above function

""" Let us create following BST
		50
	 /		\
	30		70
	/ 	\   / 	\
	20 	40	60 	80
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);

findPreSuc.pre = findPreSuc.suc = None
key = 30
findPreSuc(root, key)
print "Predecessor of {key} is {pre}, and Successor of {key} is {suc}".format(key=key,
      pre=findPreSuc.pre.key,
      suc=findPreSuc.suc.key)