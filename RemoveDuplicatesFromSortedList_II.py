# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode()
        dummy.next = head
        
        while pre.next:
            cur = pre.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            
            if cur != pre.next:
                pre.next = cur.next
            else:
                pre = cur
        
        return dummy.next


"""
Visualization of steps

dummy -> 1->1->1->2->3
 pre
        cur
-----------------------
dummy -> 1->1->1->2->3
 pre
              cur
Removing all duplicates by pre.next = cur.next  
-----------------------
dummy ->2->3
pre
       cur
-----------------------
dummy ->2->3
       pre
       cur
-----------------------
dummy ->2->3
       pre
          cur
-----------------------
dummy ->2->3
          pre
          cur
DONE !
return dummy.next
"""