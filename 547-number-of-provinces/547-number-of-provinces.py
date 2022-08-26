class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(isConnected,r, visited):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] ==1 and (c not in visited):
                    visited.add(c)
                    dfs(isConnected, c,visited)
        for r in range(len(isConnected)):
            if r not in visited:
                count+=1
                dfs(isConnected,r,visited)
        return count
        