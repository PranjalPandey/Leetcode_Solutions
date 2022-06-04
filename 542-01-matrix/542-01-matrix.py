from collections import deque
class Solution:                    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        inf = 10**9
        rows = len(mat)
        cols = len(mat[0])
        visited = [[inf for i in range(cols)] for j in range(rows)]
        
        xy = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    q.append((r,c))
                    visited[r][c]=0
                else:
                    visited[r][c] = inf
        
        
        while q:
            x, y = q.popleft()
            for dx, dy in xy:
                xx = x + dx
                yy = y + dy

                if xx >= 0 and xx < len(mat) and yy >= 0 and yy < len(mat[0]) and visited[xx][yy] != 0 \
                        and visited[xx][yy]>visited[x][y]+1:
                    visited[xx][yy] = visited[x][y]+1
                    q.append((xx, yy))
        return visited
                    