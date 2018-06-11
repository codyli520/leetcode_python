# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = [root]
        
        # 把节点从根-左-右放进stack，pop一个之后放在output最前面，输出
        # pop的顺序因为是根-右-左，反过来放到list，输出的就是左-右-根
        if not root:
            return output
        
        while stack:
            cur_node = stack.pop()
            output.insert(0,cur_node.val)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        
        return output
            
        
        
#         self.output = []
#         self.traverse(root)
#         return self.output
    
#     def traverse(self, root):
#         if not root:
#             return
        
#         self.traverse(root.left)
#         self.traverse(root.right)
#         self.output.append(root.val)
#         return