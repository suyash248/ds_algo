from commons.commons import insert, Node, print_tree

class BSTSerializationV1(object):

    def __preorder__(self, root, serialized_tree=[]):
        if root is not None:
            serialized_tree.append(root.key)
            self.__preorder__(root.left, serialized_tree)
            self.__preorder__(root.right, serialized_tree)

    def serialize(self, root):
        serialized_tree = []
        self.__preorder__(root, serialized_tree)
        return serialized_tree

    def deserialize(self, serialized_tree):
        root = self.__deserialize__(serialized_tree, 0, len(serialized_tree)-1)
        return root

    def partition(self, key, serialized_tree, start, end):
        p_index = -1
        for i in range(start, end+1):
            if serialized_tree[i] > key:
                p_index = i
                break
        # If p_index is -1 then it means, left partition(left subtree) will be null. root will have right-subtree only.
        return p_index

    # Time complexity: O(n^2)
    def __deserialize__(self, serialized_tree, start, end):
        if end < start:
            return None
        root = Node(serialized_tree[start])
        p_index = self.partition(root.key, serialized_tree, start+1, end)

        if p_index >= 0:
            # p_index is +ve, Left sub-tree: (start+1 to p_index-1(. Right sub-tree: (start+1 to end).
            root.left = self.__deserialize__(serialized_tree, start+1, p_index-1)
            root.right = self.__deserialize__(serialized_tree, p_index, end)
        else:
            # p_index is -ve, it indicates that left-subtree is null. Right sub-tree: (start+1 to end)
            root.left = None
            root.right = self.__deserialize__(serialized_tree, start+1, end)

        return root


if __name__ == '__main__':
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
    obj = BSTSerializationV1()
    serialized_tree = obj.serialize(root)
    print "Serialized Tree (Preorder) -", serialized_tree

    print "\n************* DE-SERIALIZATION *************\n"
    deserialized_tree_root = obj.deserialize(serialized_tree)

    print "\nOutput Tree - \n"
    print_tree(deserialized_tree_root)