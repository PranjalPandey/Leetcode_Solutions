from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        c = dict(Counter(nums))
        for k,v in c.items():
            if v==2:
                ans.append(k)
        return ans