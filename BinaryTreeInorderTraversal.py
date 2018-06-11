# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = []
        
        # 把最左的节点都加到stack
        while root:
            stack.append(root)
            root = root.left
            
        # pop一个节点，之后判断这个节点右边有没有，有的话把右边的和右边左节点都加到stack
        while stack:
            cur_node = stack.pop()
            output.append(cur_node.val)
   
            if cur_node.right:
                cur_node = cur_node.right
                while cur_node:
                    stack.append(cur_node)
                    cur_node = cur_node.left
        
        return output
 
#         self.output = []
#         self.traverse(root)
#         return self.output
    
#     def traverse(self, root):
#         if root is None:
#             return
#         self.traverse(root.left)
#         self.output.append(root.val)
#         self.traverse(root.right)
#         return