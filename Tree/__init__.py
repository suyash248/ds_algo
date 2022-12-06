from typing import TypeVar

T = TypeVar('T')


class TreeNode(object):
    def __init__(self, data: T, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "{left} <-- {data} --> {right}".format(
            left="NULL" if self.left is None else self.left.data,
            right="NULL" if self.right is None else self.right.data,
            data=self.data
        )


def print_tree(root: TreeNode):
    if root is None:
        return
    print(root)
    print_tree(root.left)
    print_tree(root.right)
