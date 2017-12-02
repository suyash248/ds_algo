from commons.commons import insert, print_tree, is_leaf

def all_paths_root_to_leaves_v1(root):
    if root == None:
        return
    all_paths_root_to_leaves_v1.paths.append(root.key)
    all_paths_root_to_leaves_v1(root.left)
    if root.left == None and root.right == None:
        print all_paths_root_to_leaves_v1.paths
    all_paths_root_to_leaves_v1(root.right)
    all_paths_root_to_leaves_v1.paths.pop()

def all_paths_root_to_leaves_v2(root, path, path_len):
    if root == None:
        return
    path[path_len] = root.key
    path_len += 1

    if is_leaf(root):
        for i in xrange(0, path_len):
            print path[i],
        print
    else:
        all_paths_root_to_leaves_v2(root.left, path, path_len)
        all_paths_root_to_leaves_v2(root.right, path, path_len)

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

print "\n-------- Using v1 ---------\n"
all_paths_root_to_leaves_v1.paths = []
all_paths_root_to_leaves_v1(root)

print "\n-------- Using v2 ---------\n"
all_paths_root_to_leaves_v2(root, [None] * 20, 0)