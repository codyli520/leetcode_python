# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        a_head, b_head = ListNode(0),ListNode(0)
        a_tail, b_tail = a_head, b_head
        
        while head:
            if head.val < x:
                a_tail.next = head
                a_tail = a_tail.next
            else:
                b_tail.next = head
                b_tail = b_tail.next
            head = head.next
        
        b_tail.next = None
        a_tail.next = b_head.next
        
        return a_head.next