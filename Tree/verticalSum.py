from Tree.commons import insert, Node, print_tree
from collections import OrderedDict

# Vertical sum = sum of nodes'data at same hd.
def vertical_sum(root, hd=0):
    if root is None:
        return

    vertical_sum.hm[hd] = vertical_sum.hm.get(hd, 0) + root.key
    vertical_sum(root.left, hd-1)
    vertical_sum(root.right, hd+1)


if __name__ == '__main__':
    root = Node(
        20,
        left=Node(
            8,
            left=Node(
                5
            ),
            right=Node(
                3,
                left=Node(
                    10
                ),
                right=Node(
                    14
                )
            )
        ),
        right=Node(
            22,
            left=Node(
                4
            ),
            right=Node(
                25
            )
        )
    )

    vertical_sum.hm = {}
    vertical_sum(root)
    #print vertical_sum.hm
    vertical_sum.hm = OrderedDict(sorted(vertical_sum.hm.items()))
    print("Vertical sum - ", vertical_sum.hm.values())