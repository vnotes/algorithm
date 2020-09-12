class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(l1, l2):
    soldier = ListNode(-1)
    p = soldier
    while l1 and l2:
        if l1.val > l2.val:
            p.next = l2
            l2 = l2.next
        else:
            p.next = l1
            l1 = l1.next
        p = p.next
    if not l1:
        p.next = l2
    if not l2:
        p.next = l1
    return soldier.next


def sortList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)


if __name__ == '__main__':
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    p = sortList(l1)
    q = p
    while q:
        print(q.val)
        q = q.next
