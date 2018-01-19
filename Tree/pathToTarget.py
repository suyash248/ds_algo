from commons.commons import insert, print_tree, is_leaf

def path_to_target_util_v1(root, target_key):
    if root == None:
        return False
    if root.key == target_key:
        path_to_target_v1.path.append(root.key)
        return True
    lpath = path_to_target_util_v1(root.left, target_key)
    rpath = path_to_target_util_v1(root.right, target_key)
    if lpath or rpath:
        path_to_target_v1.path.append(root.key)

    return lpath or rpath

def path_to_target_v1(root, target_key):
    path_to_target_util_v1(root, target_key)
    return path_to_target_v1.path[::-1]


def path_to_target_v2(root, target_key):
    if root == None:
        return False

    path_to_target_v2.path.append(root.key)

    if root.key == target_key:
        return True
    elif target_key < root.key:
        return path_to_target_v2(root.left, target_key)
    elif target_key > root.key:
        return path_to_target_v2(root.right, target_key)

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

    target = 40

    print "\n----------------- USING V1 -----------------\n"

    path_to_target_v1.path = []
    path_to_target_v1(root, target)
    if len(path_to_target_v1.path) > 0:
        print "Path from root {root} to node {target} is - {path}"\
            .format(root=root.key, target=target, path=path_to_target_v1.path[::-1])
    else:
        print "Target key {target} not found".format(target=target)

    print "\n----------------- USING V2 -----------------\n"

    path_to_target_v2.path = []
    is_path_exists = path_to_target_v2(root, target)
    if is_path_exists:
        print "Path from root {root} to node {target} is - {path}"\
            .format(root=root.key, target=target, path=path_to_target_v2.path)
    else:
        print "Target key {target} not found".format(target=target)

