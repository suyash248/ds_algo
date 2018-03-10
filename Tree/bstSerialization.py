from commons.commons import insert, Node, print_tree

class BSTSerialization(object):
    def __init__(self):
        self.index = 0

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
        self.index = 0
        root = self.__deserialize__(serialized_tree)
        return root

    def __deserialize__(self, serialized_tree):
        pass

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
    print_tree(root)

    obj = BSTSerialization()
    serialized_tree = obj.serialize(root)
    print serialized_tree

    deserialized_tree_root = obj.deserialize(serialized_tree)
    print_tree(deserialized_tree_root)