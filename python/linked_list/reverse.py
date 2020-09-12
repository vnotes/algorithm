class ListNode:
    def __init__(self, x):
        self.val = x
        self._next = None


def reverse_link(head):
    pass


def is_palindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next:
        return True
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    left = head
    right = self.reverse_link(slow.next)

    while left and right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
