class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr=[0 for i in range(len(nums)+1)]
        for i in nums:
            if len(arr)>i and i>0:
                arr[i]=1
        try:    
            return arr.index(0,1)
        except: 
            return len(arr)