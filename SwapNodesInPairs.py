# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        head = dummy
        
        while head.next and head.next.next:
            temp = head.next.next
            head.next.next = temp.next
            temp.next = head.next
            head.next = temp
            head = head.next.next
            
            
            
        return dummy.next
                
                