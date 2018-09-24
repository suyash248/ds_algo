from Tree.commons import insert, print_tree, is_leaf

# fs(50) - 50, fs(30)
#					fs(30) - 80, fs(20)
#									fs(20) - 100
def find_sum(root):
    if root is None:
        return 0
    return root.key + find_sum(root.left) + find_sum(root.right)

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

    print("Sum of all nodes is", find_sum(root))