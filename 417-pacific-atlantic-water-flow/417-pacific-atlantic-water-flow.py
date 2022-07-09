class Solution:                               
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()


        def dfs(visited, r, c, prevHeight):
            if ((r, c) in visited or (r < 0 or c < 0 or r == ROWS or c == COLS) or prevHeight > heights[r][c]):
                return
            visited.add((r, c))
            d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dx, dy in d:
                x = r + dx
                y = c + dy
                dfs(visited, x, y, heights[r][c])


        for c in range(COLS):
            dfs(pacific, 0, c, heights[0][c])
            dfs(atlantic, ROWS - 1, c, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(pacific, r, 0, heights[r][0])
            dfs(atlantic, r, COLS - 1, heights[r][COLS - 1])

        return sorted(list(pacific.intersection(atlantic)))
        