from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order_traversal(tree):
    if not tree:
        return
    print(tree.val)
    pre_order_traversal(tree.left)
    pre_order_traversal(tree.right)


def mid_order_traversal(tree):
    if not tree:
        return
    mid_order_traversal(tree.left)
    print(tree.val)
    mid_order_traversal(tree.right)


def post_order_traversal(tree):
    if not tree:
        return
    post_order_traversal(tree.left)

    post_order_traversal(tree.right)
    print(tree.val)


def level_order_traversal(tree):
    if not tree:
        return
    q = deque()
    q.append(tree)
    while q:
        v = q.popleft()
        print(v.val)
        if v.left:
            q.append(v.left)
        if v.right:
            q.append(v.right)


if __name__ == '__main__':
    node = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    node.left = t2
    node.right = t4
    t2.right = t3
    t4.left = t5
    pre_order_traversal(node)
    print("-" * 10)
    mid_order_traversal(node)
    print("-" * 10)
    post_order_traversal(node)
    print("-" * 10)
    level_order_traversal(node)
