"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        dic = {}
        def dfs(node):
            if not node:
                return
            else:
                node_copy = Node(node.val, [])
                dic[node] = node_copy
                for nei in node.neighbors:
                    if nei in dic:
                        node_copy.neighbors.append(dic[nei])
                    else:   
                        node_copy.neighbors.append(dfs(nei))
                return node_copy
        return dfs(node)
        