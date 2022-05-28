class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_element =  nums[0]
        max_diff = -1
        for i in range(0,len(nums)):
            if nums[i]<min_element:
                min_element=nums[i]
            if max_diff < (nums[i]-min_element):
                max_diff = (nums[i]-min_element)
        return -1 if max_diff==0 else max_diff
    
        