# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return []
        
        self.current = head
        size = 0
        while head:
            size += 1
            head = head.next
        
        return self.inorder_traverse(size)
    
    def inorder_traverse(self, size):
        if not size:
            return None
        
        left = self.inorder_traverse(size//2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.inorder_traverse(size - 1 - size//2)
        
        root.left = left
        root.right =  right
        
        return root