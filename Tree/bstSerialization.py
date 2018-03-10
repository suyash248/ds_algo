from commons.commons import insert, Node, print_tree
from Array import MAX, MIN

class BSTSerialization(object):

    def __init__(self):
        self.index = 0

    # Time complexity: O(n)
    def __preorder__(self, root, serialized_tree=[]):
        if root is not None:
            serialized_tree.append(root.key)
            self.__preorder__(root.left, serialized_tree)
            self.__preorder__(root.right, serialized_tree)

    # Time complexity: O(n)
    def serialize(self, root):
        serialized_tree = []
        self.__preorder__(root, serialized_tree)
        return serialized_tree

    # Time complexity: O(n)
    def partition(self, key, serialized_tree, start, end):
        p_index = end + 1
        for i in range(start, end+1):
            if serialized_tree[i] > key:
                p_index = i
                break
        # If p_index is (end+1) then it means, left partition(left subtree) will be null. root will have right-subtree only.
        return p_index

    # Time complexity: O(n^2)
    def deserialize_v1(self, serialized_tree):
        root = self.__deserialize_v1__(serialized_tree, 0, len(serialized_tree)-1)
        return root

    # Time complexity: O(n^2)
    def __deserialize_v1__(self, serialized_tree, start, end):
        if end < start:
            return None
        root = Node(serialized_tree[start])
        p_index = self.partition(root.key, serialized_tree, start+1, end)

        root.left = self.__deserialize_v1__(serialized_tree, start + 1, p_index - 1)
        root.right = self.__deserialize_v1__(serialized_tree, p_index, end)

        return root

    # Time complexity: O(n)
    def deserialize_v2(self, serialized_tree):
        self.index = 0
        root = self.__deserialize_v2__(serialized_tree)
        return root

    # Time complexity: O(n)
    def __deserialize_v2__(self, serialized_tree, min=MIN, max=MAX):
        if self.index >= len(serialized_tree):
            return None

        root = None
        if serialized_tree[self.index] > min and serialized_tree[self.index] < max:
            curr_elt = serialized_tree[self.index]
            self.index += 1
            root = Node(curr_elt)
            root.left = self.__deserialize_v2__(serialized_tree, min, curr_elt)
            root.right = self.__deserialize_v2__(serialized_tree, curr_elt, max)
        return root

if __name__ == '__main__':
    """
            5
        /       \
       2         7
    /    \     /   \
   1      3   6     8
            \
             4
    
    Pre-order: [5, 2, 1, 3, 4, 7, 6, 8]
    """
    root = Node(5,
                left=Node(2,
                          left=Node(1),
                          right=Node(3,
                                     right=Node(4)
                          )
                ),
                right=Node(7,
                           left=Node(6),
                           right=Node(8)
                )
            )

    print "\nInput Tree - \n"
    print_tree(root)

    print "\n************* SERIALIZATION *************\n"
    obj = BSTSerialization()
    serialized_tree = obj.serialize(root)
    print "Serialized Tree (Preorder) -", serialized_tree

    print "\n************* DE-SERIALIZATION *************\n"
    deserialized_tree_root = obj.deserialize_v2(serialized_tree)

    print "\nOutput Tree - \n"
    print_tree(deserialized_tree_root)