class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        max_count = 0
        def dfs(grid,curr,count):
            
            grid[curr[0]][curr[1]]=2
            count +=1
            d = [[1,0],[0,1],[-1,0],[0,-1]]
            for dx,dy in d:
                x = curr[0]+dx
                y = curr[1]+dy
                if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]!=1:
                    continue
                count = dfs(grid,[x,y],count)
            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count=0
                if grid[r][c]==1:
                    count = dfs(grid,[r,c],0)
                    max_count = max(max_count,count)
                    
        return max_count
                    