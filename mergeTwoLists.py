# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                    head.next = l1
                    l1 = l1.next
            else :
                head.next = l2
                l2 = l2.next

            head = head.next
        if l1:
            while l1:
                head.next = l1
                l1 = l1.next
                head = head.next

        if l2:
            while l2:
                head.next = l2
                l2 = l2.next
                head = head.next
        return head.next