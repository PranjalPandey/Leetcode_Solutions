class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for ind,l in enumerate(nums):
            nums[ind] = l**2
        return sorted(nums)