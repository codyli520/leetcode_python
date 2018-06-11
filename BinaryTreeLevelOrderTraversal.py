# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        # 用deque比list快，但不一定要用
        queue = collections.deque([root])
        result = []
        
        while queue:
            level = []
            size = len(queue)
            # 遍历到当前queue的大小，就是这一层的nodes
            # 但是queue大小会变，所以先存到size里
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            result.append(level)
        return result
                
            