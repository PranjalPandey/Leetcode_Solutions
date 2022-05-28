class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={nums[i]:i for i in range(len(nums))}
        for i,num in enumerate(nums):
            if (target-num)==num:
                    if d[num]!=i:
                        return sorted([i,d[target-num]])
                    else:
                        continue
            if (target-num) in d.keys():
                return sorted([i,d[target-num]])
            
        
                
        
        