from commons.commons import insert, print_tree, is_leaf

def lca_v1(root, key1, key2):
    from pathToTarget import path_to_target
    path_to_key1 = path_to_target(root, key1)
    path_to_key2 = path_to_target(root, key2)

    print "Path to {key1} - {path}".format(key1=key1, path=path_to_key1)
    print "Path to {key2} - {path}".format(key2=key2, path=path_to_key2)

    i = 0; lca = None
    try:
        while True:
            if path_to_key1[i] != path_to_key2[i]:
                break;
            lca = path_to_key1[i]
            i += 1
    except:
        pass
    return lca

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

key1 = 40; key2 = 15
print "LCA of {key1} & {key2} is {lca}".format(key1=key1, key2=key2, lca=lca_v1(root, key1, key2))