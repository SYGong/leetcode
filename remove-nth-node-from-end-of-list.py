class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        prev.next = head
        fast = head
        
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            prev = prev.next
        next = prev.next
        prev.next = next.next
        del next
        
        return dummy.next
