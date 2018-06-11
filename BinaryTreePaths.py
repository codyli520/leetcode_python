# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        
        if not root:
            return paths
        if not root.left and not root.right:
            paths.append(str(root.val))
        
        left_paths =  self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        
        for path in left_paths:
            paths.append(str(root.val) + "->" + path)
        for path in right_paths:
            paths.append(str(root.val) + "->" + path)
        
        return paths
    
#     def binaryTreePaths(self, root):
#         # Write your code here
#         result = []
#         if root is None:
#             return result
#         self.dfs(root, result, [])
#         return result

#     def dfs(self, node, result, tmp):
#         tmp.append(str(node.val))
#         if node.left is None and node.right is None:
#             result.append('->'.join(tmp))
#             tmp.pop()
#             return

#         if node.left:
#             self.dfs(node.left, result, tmp);
        
#         if node.right:
#             self.dfs(node.right, result, tmp)

#         tmp.pop()