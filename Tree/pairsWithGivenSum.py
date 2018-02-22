from commons.commons import insert, print_tree, is_leaf

def find(root, key):
    if root is None:
        return None
    if key < root.key:
        return find(root.left, key)
    elif key > root.key:
        return find(root.right, key)
    else:
        return root

# Time complexity < O(nlog(n))
# Space complexity: O(1), (not considering recursion stack)
def pair_with_sum_v1(root, sum, parent=None):
    if root is None:
        return False
    parent = parent or root
    remaining = abs(sum - root.key)

    # If we don't use parent, we won't be able to find a pair if both elements of pair are at same level.
    found = find(parent, remaining)
    if found:
        return (root.key, found.key)
    else:
        found = pair_with_sum_v1(root.left, sum, root) or pair_with_sum_v1(root.right, sum, root)
    return found

def pairs_with_sum_v1(root, sum, parent=None, pairs=[]):
    if root is None:
        return False
    parent = parent or root
    remaining = abs(sum - root.key)

    # If we don't use parent, we won't be able to find a pair if both elements of pair are at same level.
    found = find(parent, remaining)
    if found:
        pair = (root.key, found.key)
        pairs.append(pair)
    pairs_with_sum_v1(root.left, sum, parent=root, pairs=pairs) or pairs_with_sum_v1(root.right, sum, parent=root, pairs=pairs)


def inorder(root, inorder_traversal=[]):
    if root:
        inorder(root.left, inorder_traversal)
        inorder_traversal.append(root.key)
        inorder(root.right, inorder_traversal)

# Time complexity: O(n)
# Space complexity: O(n)
def pairs_with_sum_v2(root, sum):
    from Array.pairsWithSumInSortedArray import find_pair
    inorder_traversal = []
    inorder(root, inorder_traversal)
    return find_pair(inorder_traversal, sum)


# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		\
        30		 70
      / 	\   / 	\
     10 	35 65 	 90
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 10)
    insert(root, 35)
    insert(root, 70)
    insert(root, 65)
    insert(root, 90)

    sum = 80

    print("\n --------------------------- Using V1 ---------------------------\n")
    pair = pair_with_sum_v1(root, sum)
    print("Pair with sum = {} is {}".format(sum, "present: " + str(pair) if pair else "not present"))

    print("\n --------------------------- Using V1 ---------------------------\n")
    pairs = []
    pairs_with_sum_v1(root, sum, pairs=pairs)
    print("Pairs with sum = {} are {}".format(sum, "present: " + str(pairs) if pair else "not present"))

    print("\n --------------------------- Using V2 ---------------------------\n")
    pairs = pairs_with_sum_v2(root, sum)
    print("Pairs with sum = {} are {}".format(sum, "present: " + str(pairs) if pairs else "not present"))