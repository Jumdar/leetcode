# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    n = 0
    tmp = head
    while tmp != None:
        n += 1
        tmp = tmp.next
    pos = n - k % n
    tmp = head
    while pos > 0:
        tmp = tmp.next
        pos -= 1

    after = tmp.next
    tmp.next = None
    new_head = after
    while after.next != None:
        after = after.next
    after.next = head
    return new_head
