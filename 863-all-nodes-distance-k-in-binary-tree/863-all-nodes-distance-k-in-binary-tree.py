# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        visited = set()
        ans = []
        graph = defaultdict(list)
        
        def make_graph(node,parent,graph):
            if node is None:
                return
            if parent:
                graph[node].append(parent)
            
            if node.right:
                graph[node].append(node.right)
                make_graph(node.right,node,graph)
            
            if node.left:
                graph[node].append(node.left)
                make_graph(node.left,node,graph)
                
        make_graph(root,None,graph)
        q = deque()
        q.append((target,0))
        while q:
            t,d = q.popleft()
            visited.add(t)
            if d==k:
                ans.append(t.val)
            for neigh in graph[t]:
                if neigh not in visited:
                    q.append((neigh,d+1))
        return ans
                