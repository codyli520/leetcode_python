# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = []
        cur = root
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        
        
        while stack:
            next_node = stack.pop()
            cur.right = next_node
            cur.left = None
            cur = next_node
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
            
                
#         self.helper(root)
        
#     def helper(self,root):
#         if not root:
#             return None
        
#         leftLast = self.helper(root.left)
#         rightLast = self.helper(root.right)
        
#         if leftLast:
#             leftLast.right = root.right
#             root.right = root.left
#             root.left = None
            
#         if rightLast:
#             return rightLast
        
#         if leftLast:
#             return leftLast
        
#         return root