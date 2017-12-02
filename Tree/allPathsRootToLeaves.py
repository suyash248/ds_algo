# Python program to find predecessor and successor in a BST

# A BST node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A utility function to insert a new node in with given key in BST
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    else:
        node.right = insert(node.right, key)

    return node

def all_paths_root_to_leaves(root):
    if root == None:
        return
    all_paths_root_to_leaves.paths.append(root.key)
    all_paths_root_to_leaves(root.left)
    if root.left == None and root.right == None:
        print all_paths_root_to_leaves.paths
    all_paths_root_to_leaves(root.right)
    all_paths_root_to_leaves.paths.pop()

def path_to_target(root, target_key):
    if root == None:
        return False
    if root.left == None and root.right == None:
        path_to_target.paths.append(root.key)
        return True
    lpath = path_to_target(root.left, target_key)
    rpath = path_to_target(root.right, target_key)
    if lpath or rpath:
        path_to_target.paths.append(root.key)

    return lpath or rpath


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
	 /		 \
	30		  70
   /  \     / 	 \
  20   40  60 	  80
 /   \
15   25
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 15);
insert(root, 25);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);

#all_paths_root_to_leaves.paths = []
#all_paths_root_to_leaves(root)

path_to_target.paths = []
path_to_target(root, 60)
print path_to_target.paths[::-1]
#print_tree(root)