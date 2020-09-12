import math

k = 0


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst(node, l, r):
    global k
    k += 1
    if not node:
        return True
    if l >= node.val or r <= node.val:
        return False
    x = bst(node.left, l, node.val)
    y = bst(node.right, node.val, r)
    return x and y


def is_valid_bst(root):
    inf = math.inf
    return bst(root, -inf, +inf)


if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(7)
    t4 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t3.left = t4

    print(is_valid_bst(t1))
    print(k)
