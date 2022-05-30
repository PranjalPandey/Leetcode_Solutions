import sys
sys.setrecursionlimit(10**6)
class Solution:
    def make_permutations(self, ans, nums,i):
        if i>=len(nums):
            ans.append(nums.copy())
            return
        #J signifies number of nodes and i signifies number of level of the recursion tree
        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            self.make_permutations(ans,nums,i+1)
            nums[i],nums[j]=nums[j],nums[i]
                       
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        self.make_permutations(ans,nums,0)
        return ans