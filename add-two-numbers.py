# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        exceed_ten = False
        while l1 and l2:
            sum_two = l1.val + l2.val
            if exceed_ten:
                sum_two += 1
                exceed_ten = False
            if sum_two >= 10:
                exceed_ten = True
            cur.next = ListNode(sum_two % 10)
            cur = cur.next
            l1, l2 = l1.next, l2.next
        
        while l1 or l2:
            val = l1.val if l1 else l2.val
            if exceed_ten:
                val += 1
                exceed_ten = False
            if val == 10:
                val = 0
                exceed_ten = True
            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            else:
                l2 = l2.next
        if exceed_ten:
            cur.next = ListNode(1)
        return dummy.next