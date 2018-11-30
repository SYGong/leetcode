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
        eval_ = lambda l: 0 if l is None else l.val
        next_ = lambda l: None if l is None else l.next
        curr = dummy_head = ListNode(0)  
        carry = 0 # Initiated to carry from one iteration to another
        while l1 or l2 or carry:
            sum_ = eval_(l1) + eval_(l2) + carry
            curr.next = ListNode(sum_ % 10)
            curr = curr.next
            l1 = next_(l1)
            l2 = next_(l2)
            carry = sum_ // 10
        return dummy_head.next