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
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        left_paths = self.pathSum(root.left, sum-root.val)
        right_paths = self.pathSum(root.right, sum-root.val)
        
        if not root.right and not root.left and root.val == sum:
            return [[root.val]]
        
        for path in left_paths:
            path.insert(0,root.val)
        for path in right_paths:
            path.insert(0,root.val)
        return left_paths+right_paths