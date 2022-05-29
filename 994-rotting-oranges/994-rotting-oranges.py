from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        inf=10000000000000
        dist=[[0 for j in range(m)] for i in range(n)]
        q=deque()
        li=[[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 or grid[i][j]==0):
                    dist[i][j]=inf
                else:
                    q.append([i,j])
        while(len(q)!=0):
            x,y=q.popleft()
            for k in range(4):
                dx=x+li[k][0]
                dy=y+li[k][1]
                if(dx>=0 and dy>=0 and dx<n and dy<m and grid[dx][dy]==1 and dist[x][y] +1 <dist[dx][dy] ):
                    dist[dx][dy]=dist[x][y] +1
                    q.append([dx,dy])
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    ans=max(ans,dist[i][j])
        if(ans==inf):
            return -1
        return ans
        # row = len(grid)
        # if row is 0:
        #     return -1
        # col = len(grid[0])
        # rotten_oranges = deque()
        # fresh_count=0
        # for r in range(row):
        #     for c in range(col):
        #         if grid[r][c]==2:
        #             rotten_oranges.append((r,c))
        #         elif grid[r][c]==1:
        #             fresh_count+=1
        # time_elapsed=0
        # while rotten_oranges and fresh_count>0:
        #     time_elapsed+=1
        #     for p in range(len(rotten_oranges)):
        #         x,y = rotten_oranges.popleft()
        #         for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        #             xx = x+dx
        #             yy = y+dy
        #             if xx>row-1 or yy>col-1 or xx<0 or yy<0:
        #                 continue
        #             if grid[xx][yy]==1:
        #                 fresh_count-=1
        #                 grid[xx][yy] = 2
        #                 rotten_oranges.append((xx,yy))
        # return time_elapsed if fresh_count==0 else -1
            