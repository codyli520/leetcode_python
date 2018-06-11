# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        root = node
        nodes = self.helper(node)
        
        mappings = {} # old node : new node
        
        for n in nodes:
            mappings[n] = UndirectedGraphNode(n.label)
        
        for n in nodes:
            new_node = mappings[n]
            for neighbor in n.neighbors:
                new_neighbors = mappings[neighbor]
                new_node.neighbors.append(new_neighbors)
        
        return mappings[root]
            
        
        
    
    def helper(self, node):
        queue = collections.deque([node])
        result = set([node])
        
        while queue:
            cur_node = queue.popleft()
            result.add(cur_node)
            
            for n in cur_node.neighbors:
                if n not in result:
                    queue.append(n)

        return result