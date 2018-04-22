from commons.commons import insert, print_tree, is_leaf

def lca_v1(root, key1, key2):
    from pathToTarget import path_to_target_v1
    path_to_key1 = path_to_target_v1(root, key1)
    path_to_key2 = path_to_target_v1(root, key2)

    print "Path to {key1} - {path}".format(key1=key1, path=path_to_key1)
    print "Path to {key2} - {path}".format(key2=key2, path=path_to_key2)

    i = 0; lca = None
    try:
        while True:
            if path_to_key1[i] != path_to_key2[i]:
                break
            lca = path_to_key1[i]
            i += 1
    except:
        pass
    return lca


lca_found = False
def lca_v2(root, key1, key2):
    global lca_found
    if root is None:
        return None

    if root.key == key1 or root.key == key2:
        return root

    lpath = lca_v2(root.left, key1, key2)
    rpath = lca_v2(root.right, key1, key2)

    if lpath is not None and rpath is not None:
        lca_found = True
        return root # This is LCA

    return lpath or rpath

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
    insert(root, 30)
    insert(root, 20)
    insert(root, 15)
    insert(root, 25)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    key1 = 40; key2 = 15

    print "\n----- Using V1 -----\n"
    print "LCA of {key1} & {key2} is {lca}".format(key1=key1, key2=key2, lca=lca_v1(root, key1, key2))

    print "\n----- Using V2 -----\n"
    lca_node = lca_v2(root, key1, key2)
    lca = lca_node.key if lca_found else None
    print "LCA of {key1} & {key2} is {lca}".format(key1=key1, key2=key2, lca=lca)