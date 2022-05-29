from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row is 0:
            return -1
        col = len(grid[0])
        rotten_oranges = deque()
        fresh_count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    rotten_oranges.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1
        time_elapsed=0
        while rotten_oranges and fresh_count>0:
            time_elapsed+=1
            for p in range(len(rotten_oranges)):
                x,y = rotten_oranges.popleft()
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    xx = x+dx
                    yy = y+dy
                    if xx>row-1 or yy>col-1 or xx<0 or yy<0:
                        continue
                    if grid[xx][yy]==1:
                        fresh_count-=1
                        grid[xx][yy] = 2
                        rotten_oranges.append((xx,yy))
        return time_elapsed if fresh_count==0 else -1
            