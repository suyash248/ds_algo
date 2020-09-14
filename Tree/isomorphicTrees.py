from Tree.commons import Node, print_tree, is_leaf

# https://www.geeksforgeeks.org/tree-isomorphism-problem/

def check_isoporphism(root1: Node, root2: Node) -> bool:
    if root1 is None and root2 is None: # both are None
        return True
    if root1 is None or root2 is None:  # Any one of them is None
        return False
    if root1.key != root2.key:    # data doesn't match
        return False

    return (
        (check_isoporphism(root1.left, root2.left) and check_isoporphism(root1.right, root2.right)) or # Not flipped
        (check_isoporphism(root1.left, root2.right) and check_isoporphism(root1.right, root2.left)) # Flipped
    )



if __name__ == '__main__':
    '''
            2               
        3        4
     5     6  7     8  
     
             2               
        4        3
     8     7  5     6  
    
    '''

    root1: Node = Node(2, left=Node(3, left=Node(5), right=Node(6)), right=Node(4, left=Node(7), right=Node(8)))
    root2: Node = Node(2, left=Node(4, left=Node(8), right=Node(7)), right=Node(3, left=Node(5), right=Node(6)))

    print("Tree: 1")
    print_tree(root1)

    print("\nTree: 2")
    print_tree(root2)

    are_isomorphic = check_isoporphism(root1, root2)
    print(are_isomorphic)