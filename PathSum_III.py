# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        return self.countPath(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def countPath(self, root, sum):
        if not root:
            return 0
        
        res = 0
        if root.val == sum:
            res += 1
            
        res += self.countPath(root.left, sum-root.val)
        res += self.countPath(root.right, sum-root.val)
        
        
        return res