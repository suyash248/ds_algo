from collections import deque

from Tree import TreeNode, print_tree


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data is None or len(data) == 0:
        return None

    data = data.split(",")
    q = deque()
    root = TreeNode(data[0])
    q.append(root)
    i = 1
    
    while i < len(data):
        parent = q.popleft()
        if data[i] != '#':
            parent.left = TreeNode(data[i])
            q.append(parent.left)
        i += 1
        if data[i] != '#':
            parent.right = TreeNode(data[i])
            q.append(parent.right)
        i += 1
    return root

if __name__ == '__main__':
    print_tree(deserialize("1,2,3,#,#,4,5"))