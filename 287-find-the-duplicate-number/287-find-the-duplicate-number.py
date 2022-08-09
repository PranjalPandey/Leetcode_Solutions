class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = [0 for i in range(len(nums)+1)]
        for n in nums:
            l[n]+=1
            if l[n] ==2:
                return n
        