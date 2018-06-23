# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode(-1)
        dummy.next = head
        
        head = dummy
        
        while True:
            head = self.reverse(head, k)
            if head is None:
                break
        
        return dummy.next
    
    def reverse(self, head, k):
        node_k = head
        for i in range(k):
            if node_k is None:
                return None
            node_k = node_k.next
        
        if node_k is None:
            return None
        
        prev = None
        cur = head.next
        start_node = head.next
        post_node_k = node_k.next
        
        for i in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        head.next = node_k
        start_node.next = post_node_k
        
        return start_node
        