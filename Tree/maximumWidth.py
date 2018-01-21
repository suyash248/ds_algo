from commons.commons import insert
from treeHeight import calculate_height
from Array import empty_1d_array

# Time Complexity: O(n)
# Space Complexity: O(n)
def maximum_width_using_level_order_traversal(root):
    from Queue import Queue
    q = Queue()
    q.put(root)
    max_width = 0
    while not q.empty():
        count = q.qsize()
        max_width = max(max_width, count)

        while count > 0:
            count -= 1
            popped_elt = q.get()
            if popped_elt.left: q.put(popped_elt.left)
            if popped_elt.right: q.put(popped_elt.right)
    return max_width


# Time Complexity: O(n)
# Space Complexity: O(h) or O(log(n))
def maximum_width_using_pre_order_traversal(root, level=0):
    global counts_arr
    if root is None:
        return
    counts_arr[level] += 1
    maximum_width_using_pre_order_traversal(root.left, level+1)
    maximum_width_using_pre_order_traversal(root.right, level+1)


if __name__ == '__main__':
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

    print "Maximum width of tree is - ", maximum_width_using_level_order_traversal(root)

    tree_height = calculate_height(root)
    counts_arr = empty_1d_array(tree_height, fill_default=0)
    maximum_width_using_pre_order_traversal(root)
    print "Maximum width of tree is - ", max(counts_arr)
