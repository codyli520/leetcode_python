# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        complement = []
        
        queue = [root]
        
        while queue:
            cur = queue.pop(0)
            if cur.val in complement:
                return True
            else:
                complement.append(k-cur.val)
            
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        
        return False
            