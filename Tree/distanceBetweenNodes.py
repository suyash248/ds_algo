from commons.commons import insert, print_tree, is_leaf

# Driver program to test above function
if __name__ == "__main__":
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

    print "\n----- Using V1 -----\n"
    print "LCA of {key1} & {key2} is {lca}".format(key1=key1, key2=key2, lca=lca_v1(root, key1, key2))

    print "\n----- Using V2 -----\n"
    lca_node = lca_v2(root, key1, key2)
    lca = lca_node.key if lca_found else None
    print "LCA of {key1} & {key2} is {lca}".format(key1=key1, key2=key2, lca=lca)