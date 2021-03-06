from Tree.commons import insert, print_tree, is_leaf

def is_sum_equal(root, total, sum=0):
    if root is None:
        return False
    sum += root.key

    if is_leaf(root) and total == sum:
        return True

    return is_sum_equal(root.left, total, sum) or is_sum_equal(root.right, total, sum)

def all_paths_with_sum(root, total, path, path_len=0):
    if root == None:
        return
    path[path_len] = root.key
    path_len += 1

    if is_leaf(root) and sum(path[0:path_len]) == total:
        all_paths_with_sum.paths_with_sum.append(path[0:path_len])
    else:
        all_paths_with_sum(root.left, total, path, path_len=path_len)
        all_paths_with_sum(root.right, total, path, path_len=path_len)




# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		\
        30		70
        / 	\   / 	\
        20 	40	60 	80
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    total = 120
    res = is_sum_equal(root, total, 0)
    print("Does path with sum {total} exists? - {res}".format(total=total, res=res))

    all_paths_with_sum.paths_with_sum = []
    all_paths_with_sum(root, total, [None] * 20)
    print("Path(s) with sum {total} - {paths}".format(total=total, paths=all_paths_with_sum.paths_with_sum))