# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        cur = head
        seen = set([cur.val])
        while cur.next:
            if cur.next.val in seen:
                cur.next = cur.next.next
            else:
                cur = cur.next
                seen.add(cur.val)
        
        return head