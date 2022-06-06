class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        row = 1
        while row<m:
            dp[0] = 1
            for i in range(1,n):
                dp[i] = dp[i-1]+dp[i]
            row+=1
        return dp[-1]