from commons.commons import insert, print_tree, is_leaf

def path_to_target_util(root, target_key):
    if root == None:
        return False
    if root.key == target_key:
        path_to_target.path.append(root.key)
        return True
    lpath = path_to_target_util(root.left, target_key)
    rpath = path_to_target_util(root.right, target_key)
    if lpath or rpath:
        path_to_target.path.append(root.key)

    return lpath or rpath

def path_to_target(root, target_key):
    path_to_target.path = []
    path_to_target_util(root, target_key)
    return path_to_target.path[::-1]

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

    target = 60
    path_to_target(root, target)

    print "Path to node {target} is - {path}".format(target=target, path=path_to_target.path[::-1])
