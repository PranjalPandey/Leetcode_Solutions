class Solution:
    def dfs(self,grid,r,c,m,n):
        if r==m:
            return c
        if c+1<n and grid[r][c]==1 and grid[r][c+1]==1:
            return self.dfs(grid,r+1,c+1,m,n)
        if c-1>=0 and grid[r][c]==-1 and grid[r][c-1]==-1:
            return self.dfs(grid,r+1,c-1,m,n)
        return -1
        
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = [self.dfs(grid,0,j,m,n) for j in range(n)]
        return ans