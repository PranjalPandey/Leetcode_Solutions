class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = dict(Counter(nums)) 
        k = len(d)
        for ind,num in enumerate(sorted(list(d.keys()))):
            nums[ind] = num
        for ind in range(k,len(nums)):
            nums[ind]= "_"
            
        return k
            
        
      