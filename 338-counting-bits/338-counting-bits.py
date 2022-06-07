class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n+1)]
        dp[0]=0
        for i in range(1,n+1):
            fix = int(math.log(i, 2))
            not_fixed=i-(2**fix)
            if not_fixed!=0:
                dp[i]=dp[ref]+dp[not_fixed]
            else:
                ref = i
                dp[i] = 1
        return dp
        