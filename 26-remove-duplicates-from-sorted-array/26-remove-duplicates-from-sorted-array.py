class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        for ind in range(len(nums)-1):
            if nums[ind] != nums[ind+1]:
                nums[k]=nums[ind+1]
                k+=1
        return k
            
            
        
      