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
        for i in range(n):
            curr_node = curr_node.next
        if not curr_node:
            return head.next
        while curr_node.next:
            curr_node = curr_node.next
            Np1th_from_curr = Np1th_from_curr.next
        Np1th_from_curr.next = Np1th_from_curr.next.next
        return head
