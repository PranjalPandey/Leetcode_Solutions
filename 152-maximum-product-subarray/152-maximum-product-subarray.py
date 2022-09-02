class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_so_far = nums[0]
        # max_here = nums[0]
        # min_here = nums[0]
        # for i in range(1,len(nums)):
        #     t = max(max(nums[i],nums[i]*max_here),nums[i]*min_here)
        #     min_here = min(min(nums[i],nums[i]*max_here),nums[i]*min_here)
        #     max_here = t
        #     max_so_far = max(max_so_far,max_here)
        # return max_so_far
        
        curr_max,curr_min,ans=0,0,-1*sys.maxsize
        for i in nums:
            if i>0:
                curr_max,curr_min=max(i,i*curr_max),min(i,i*curr_min)
            else:
                curr_max,curr_min=max(i,i*curr_min),min(i,i*curr_max)
            ans=max(ans,curr_max)
        return ans if ans else max(nums)