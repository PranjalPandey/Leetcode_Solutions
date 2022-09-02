class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_here = nums[0]
        min_here = nums[0]
        for i in range(1,len(nums)):
            t = max(max(nums[i],nums[i]*max_here),nums[i]*min_here)
            min_here = min(min(nums[i],nums[i]*max_here),nums[i]*min_here)
            max_here = t
            max_so_far = max(max_so_far,max_here)
        return max_so_far