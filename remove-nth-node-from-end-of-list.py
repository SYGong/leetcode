# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        Np1th_from_curr = head
        curr_node = head
        while curr_node.next:
            curr_node = curr_node.next
            if n > 0:
                n -= 1
            else:
                Np1th_from_curr = Np1th_from_curr.next
        Np1th_from_curr.next = Np1th_from_curr.next.next
        
            