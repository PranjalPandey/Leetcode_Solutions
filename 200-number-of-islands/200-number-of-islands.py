class Solution:
    def dfs(self, grid, r, c, visited):
        visited[r][c]=1
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        for dx,dy in d:
            xx = r+dx
            yy = c+dy
            if xx>len(grid)-1 or yy>len(grid[0])-1 or xx<0 or yy<0:
                continue
            if visited[xx][yy]!=1 and grid[xx][yy]=="1":
                self.dfs(grid,xx,yy,visited)
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        row = len(grid)
        col = len(grid[0])
        visited  = [[0 for i in range(col)] for i in range(row)]
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and visited[r][c]!=1:
                    number_of_islands+=1
                    self.dfs(grid,r,c,visited)
        return number_of_islands
        