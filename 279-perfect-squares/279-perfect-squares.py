class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10**9 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        arr = []
        k=1
        while k*k<=n:
            arr.append(k*k)
            dp[k*k]=1
            k+=1
        for i in range(2,n+1):
            for j in range(len(arr)-1,-1,-1):
                if (i-arr[j])>0:
                    dp[i] = min(dp[i],dp[i-arr[j]]+1)
        return dp[n]