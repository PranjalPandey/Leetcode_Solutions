class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10**9 for i in range(len(nums))]
        dp[0] = 0
        for ind,num in enumerate(nums):
            for i in range(num+1):
                if (ind+i)<len(nums):
                    dp[ind+i] = min(dp[ind+i],dp[ind]+1)
        print(dp)
        return dp[-1]
            
        