# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = []
        isOver = False
        while l1 is not None or l2 is not None:
            if l1 is None:
                x1 = 0
                x2 = l2.val
            elif l2 is None:
                x1 = l1.val
                x2 = 0
            else:
                x1 = l1.val
                x2 = l2.val
            temp = x1 + x2
            if isOver:
                temp = temp + 1
                isOver = False
            if temp >= 10:
                temp = temp - 10
                isOver = True
            list.append(temp)
            if l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        if isOver:
            list.append(1)
        head = ListNode(list[len(list) - 1])
        for i in range(len(list) - 1):
            result = ListNode(list[len(list) - i - 2])
            result.next = head
            head = result
        return head

