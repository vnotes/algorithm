class ListNode:
    def __init__(self, val):
        self.val = val
        self._next = None


def get_intersection_node(headA, headB):
    p, q = headA, headB
    if not p or not q:
        return None
    while p != q:
        p = p._next if p else headB
        q = q._next if q else headA
    return p


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(6)
    l3 = ListNode(7)
    l4 = ListNode(10)
    l5 = ListNode(4)
    l6 = ListNode(10)
    l7 = ListNode(9)
    l8 = ListNode(1)

    l1._next = l2
    l2._next = l3
    l3._next = l4

    l5._next = l4
    l6._next = l7
    l7._next = l2
    l7._next = l8

    k = get_intersection_node(l1, l5)
    print(k.val)
