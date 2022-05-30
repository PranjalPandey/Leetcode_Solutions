import sys
sys.setrecursionlimit(10**6)
class Solution:
    def make_permutations(self, ans, nums,i):
        if i>=len(nums):
            ans.append(nums.copy())
            return
        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            self.make_permutations(ans,nums,i+1)
            nums[i],nums[j]=nums[j],nums[i]
                       
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        self.make_permutations(ans,nums,0)
        return ans