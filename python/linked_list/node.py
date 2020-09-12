class ListNode:
    def __init__(self, val):
        self.val = val
        self._next = None


# 4->2->5->8
def reversed_linked(linked):
    pre = None
    while linked:
        n = linked._next
        linked._next = pre
        pre = linked
        linked = n
    return pre


if __name__ == '__main__':
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(5)
    l4 = ListNode(8)
    l1._next = l2
    l2._next = l3
    l3._next = l4
    l0 = reversed_linked(l1)
    print(l0)
