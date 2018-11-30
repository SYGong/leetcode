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
        carry = 0
        prev = curr = head = ListNode(carry)  
        while l1 or l2 or carry:
            sum_ = eval_(l1) + eval_(l2) + curr.val
            curr.val = sum_ % 10
            l1 = next_(l1)
            l2 = next_(l2)
            carry = sum_ // 10
            curr.next = ListNode(carry)  # Created without condition l1 or l2 or carry
            prev = curr
            curr = curr.next
        if curr.val == 0:
            prev.next = None  # then have to trim the tail
        return head