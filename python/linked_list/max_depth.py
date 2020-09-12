class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    rs = 0
    q = [root]
    while q:
        l = len(q)
        for _ in range(l):
            t = q.pop(0)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        rs += 1
    return rs


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5
    rs = max_depth(t1)
    print(rs)
