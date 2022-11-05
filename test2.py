from test import Node, print_tree
from collections import deque

def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data is None or len(data) == 0:
        return None

    data = data.split(",")
    q = deque()
    root = Node(data[0])
    q.append(root)
    i = 1
    
    while i < len(data):
        parent = q.popleft()
        if data[i] != '#':
            parent.left = Node(data[i])
            q.append(parent.left)
        i += 1
        if data[i] != '#':
            parent.right = Node(data[i])
            q.append(parent.right)
        i += 1
    return root

if __name__ == '__main__':
    print_tree(deserialize("1,2,3,#,#,4,5"))