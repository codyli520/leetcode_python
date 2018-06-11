# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        is_left = True
        result = []
        queue = collections.deque([root])
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()
                if is_left:
                    level.append(node.val)
                else:
                    level.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_left = not is_left
            result.append(level)
        return result