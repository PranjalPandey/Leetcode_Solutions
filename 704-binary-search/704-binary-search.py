class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        mid = (high-low)+low//2
        while low<=high:
            mid = (high-low)+low//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1 