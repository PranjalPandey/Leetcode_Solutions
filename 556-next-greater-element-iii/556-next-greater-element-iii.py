class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        nums = list(str(n))
        i = j = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return -1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:]= nums[len(nums)-1:i-1:-1]
        return "".join(nums) if (int("".join(nums)) is not None) and (int("".join(nums))< 2147483648) else -1