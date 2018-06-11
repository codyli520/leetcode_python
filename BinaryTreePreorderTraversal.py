# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Non-recursive
        stack = [root]
        output = []
        
        while stack:
            # 先放右再放左，pop出来左边，再放左边的右儿子，再左儿子...etc..
            # 根-左-右
            cur_node = stack.pop()
            if cur_node is not None:
                output.append(cur_node.val)
                stack.append(cur_node.right)
                stack.append(cur_node.left)
                
        return output
    
    ''' recursive
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.output = []
        self.traverse(root)
        return self.output
    
    def traverse(self, root):
        if root is None is None:
            return
        self.output.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        return
    '''
        