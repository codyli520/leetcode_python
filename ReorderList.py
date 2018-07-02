# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = slow.next
        slow.next = None
        
        # Reverse
        prev = None
        cur = second_half_head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            second_half_head = prev
        
        # Merge
        while second_half_head:
            temp_1 = head.next
            temp_2 =  second_half_head.next
            head.next = second_half_head
            second_half_head.next = temp_1
            head = temp_1
            second_half_head = temp_2
        