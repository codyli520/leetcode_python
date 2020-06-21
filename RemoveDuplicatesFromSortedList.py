# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur is not None:
            temp = cur
            while temp.next and temp.val == temp.next.val:
                temp = temp.next
            cur.next = temp.next
            cur = temp.next
        return head
        