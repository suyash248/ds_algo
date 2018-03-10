from commons.commons import insert, Node, print_tree

class BinaryTreeSerialization(object):
    def __init__(self, delimiter=None):
        self.delimiter = delimiter
        self.index = 0

    def __preorder__(self, root, serialized_tree=[]):
        if root is None:
            serialized_tree.append(self.delimiter)
            return None

        serialized_tree.append(root.key)
        self.__preorder__(root.left, serialized_tree)
        self.__preorder__(root.right, serialized_tree)

    def serialize(self, root):
        serialized_tree = []
        self.__preorder__(root, serialized_tree)
        return serialized_tree

    def deserialize(self, serialized_tree):
        self.index = 0
        root = self.__deserialize__(serialized_tree)
        return root

    def __deserialize__(self, serialized_tree):
        if self.index >= len(serialized_tree) or serialized_tree[self.index] == self.delimiter:
            self.index += 1
            return None
        root = Node(serialized_tree[self.index])
        self.index += 1

        root.left = self.__deserialize__(serialized_tree)
        root.right = self.__deserialize__(serialized_tree)
        return root

if __name__ == '__main__':
    root = Node(7,
                left=Node(2,
                          left=Node(1)
                ),
                right=Node(5,
                           left=Node(3),
                           right=Node(8)
                )
            )

    print "\nInput Tree - \n"
    print_tree(root)

    print "\n************* SERIALIZATION *************\n"
    obj = BinaryTreeSerialization()
    serialized_tree = obj.serialize(root)
    print "Serialized Tree (Preorder) -", serialized_tree

    print "\n************* DE-SERIALIZATION *************\n"
    deserialized_tree_root = obj.deserialize(serialized_tree)

    print "\nOutput Tree - \n"
    print_tree(deserialized_tree_root)