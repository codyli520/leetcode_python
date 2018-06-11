# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        stack = []
        
        # inorder traversal
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
                node = cur.right
                while node.left:
                    node = node.left
                    stack.append(node)
            
            # if current element is less than the previous element
            if len(result) > 0 and cur.val <= result[-1]:
                return False
            
            result.append(cur.val)
        
        return True
                
            