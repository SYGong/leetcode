class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = l1
        pre = dummy
        carry = 0
        while l1 and l2:
            carry += l1.val+l2.val
            l1.val = carry % 10
            carry = carry // 10
            l1 = l1.next
            l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        elif l2:
            pre.next = l2
        while pre and pre.next:
            carry += pre.next.val
            pre.next.val = carry % 10
            carry = carry // 10
            pre = pre.next
        if carry:
            pre.next = ListNode(carry)
        return dummy.next
            