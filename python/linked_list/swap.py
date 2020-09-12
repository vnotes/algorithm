class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self._next = _next


def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head._next:
        return head
    f, r = head, head._next
    f._next = None
    r._next = f
    return head


# 1->2

if __name__ == '__main__':
    l = ListNode(1, ListNode(2))
    rs = swap_pairs(l)
    print(rs)
