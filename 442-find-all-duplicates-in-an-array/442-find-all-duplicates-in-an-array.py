from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #With Extra space
        ans = []
        # c = dict(Counter(nums))
        # for k,v in c.items():
        #     if v==2:
        #         ans.append(k)
        
        
        # without extra space
        for num in nums:
            if nums[abs(num)-1]<0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1]*=-1
        return ans
        