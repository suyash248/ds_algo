from Tree.commons import insert

def distance_between_nodes(root, key1, key2):
    """
    Dist(key1, key2) = Dist(root, key1) + Dist(root, key2) - 2*Dist(root, lca)
    Where lca is lowest common ancestor of key1 & key2
    :param root:
    :param key1:
    :param key2:
    :return:
    """
    from Tree.distanceFromRoot import distance_from_root_v1
    from Tree.lowestCommonAncestor import lca_v2
    d1 = distance_from_root_v1(root, key1)
    d2 = distance_from_root_v1(root, key1)
    lca = lca_v2(root, key1, key2)
    if lca is None:
        return 0    # When either of key1 or key2 is not found, distance is 0
    d_lca = distance_from_root_v1(root, lca.key)
    return (d1 + d2 - 2*d_lca)

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

    key1= 60; key2 = 30
    d = distance_between_nodes(root, key1, key2)
    print("Distance between {key1} & {key2} is {d}".format(key1=key1, key2=key2, d=d))