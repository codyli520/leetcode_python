# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = [root]
        index = 0
        
        while index < len(queue):
            if queue[index]:
                node = queue[index]
                queue.append(node.left)
                queue.append(node.right)
            index += 1
            
        while queue[-1] is None:
            queue.pop()
 
        return ','.join(str(node.val) if node is not None else '#' for node in queue)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        left_child = True
        index = 0
        
        for val in nodes[1:]:
            if val != '#':
                node = TreeNode(int(val))
                if left_child:
                    queue[index].left = node
                else:
                    queue[index].right = node

                queue.append(node)
            
            if not left_child:
                index += 1
            left_child = not left_child
        
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))