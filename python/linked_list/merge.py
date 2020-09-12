class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self._next = _next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(-1)
    p = dummy
    while l1 and l2:
        if l1.val < l2.val:
            p._next = l1
            p = p._next
            l1 = l1._next
        else:
            p._next = l2
            p = p._next
            l2 = l2._next
    if l1:
        p._next = l1
    if l2:
        p._next = l2
    return dummy._next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2))
    l2 = ListNode(3, ListNode(4))
    t = merge_two_lists(l1, l2)
    print(t)
