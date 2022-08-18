class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 'X'
        flag = False
        for c in range(cols):
            if obstacleGrid[0][c]=="X":
                flag = True
            elif flag:
                obstacleGrid[0][c] = 'X'
            else:
                obstacleGrid[0][c] = 1
        flag = False
        for r in range(rows):
            if obstacleGrid[r][0]=="X":
                flag = True
            elif flag:
                obstacleGrid[r][0] = 'X'
            else:
                obstacleGrid[r][0] = 1

                
        for r in range(1,rows):
            for c in range(1,cols):
                if obstacleGrid[r][c] != "X":
                    if obstacleGrid[r-1][c] != "X" and obstacleGrid[r][c-1] != "X":
                        obstacleGrid[r][c] = obstacleGrid[r-1][c]+obstacleGrid[r][c-1]
                    elif obstacleGrid[r-1][c] != "X":
                        obstacleGrid[r][c] = obstacleGrid[r-1][c]
                    elif obstacleGrid[r][c-1] != "X":
                        obstacleGrid[r][c] = obstacleGrid[r][c-1]
        print(obstacleGrid)
        return 0 if obstacleGrid[-1][-1]=='X' else obstacleGrid[-1][-1]