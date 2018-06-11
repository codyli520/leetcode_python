# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class ResultType:
    def __init__(self, depth, balanced):
        self.depth = depth
        self.balanced = balanced
            
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_balanced(root).balanced
    
    def is_balanced(self, root):
        if root is None:
            return ResultType(0, True)
        
        left = self.is_balanced(root.left)
        right = self.is_balanced(root.right)
        
        if not left.balanced or not right.balanced:
            return ResultType(-1,False)
        
        if abs(left.depth-right.depth) > 1:
            return ResultType(-1,False)
        
        return ResultType(max(left.depth,right.depth)+1, True)
        
        
        
        