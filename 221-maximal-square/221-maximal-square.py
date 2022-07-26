class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for c in range(len(matrix[0])+1)] for r in range(len(matrix)+1)]
        max_side = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]=="1":
                    dp[r+1][c+1] = min(dp[r][c],dp[r][c+1],dp[r+1][c])+1
                    max_side = max(max_side,dp[r+1][c+1])
                    
        return max_side*max_side
                    