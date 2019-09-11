# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        def merge(l1, l2):
            head = ListNode(0)
            prehead = head
            while l1 and l2:
                if l1.val <= l2.val:
                    prehead.next = l1
                    l1 = l1.next
                else:
                    prehead.next = l2
                    l2 = l2.next
                prehead = prehead.next
            prehead.next = l1 if l1 else l2

            return head.next

        amount = len(lists)
        interval = 1
        while interval < amount:

            for i in range(0, amount-interval, interval*2):
                lists[i] = merge(lists[i], lists[i+interval])
            interval *= 2

        return lists[0] if amount>0 else False