class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp =[False for i in range(sum(nums)//2+1)]
        dp[0] = True
        
        for num in nums:
            for n in range(sum(nums)//2,num-1,-1):
                dp[n] = dp[n] or dp[n-num]
        return dp[-1]