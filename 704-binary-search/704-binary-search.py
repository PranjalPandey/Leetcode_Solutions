class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        mid = (low)+(high-low)//2
        while low<high:
            mid = (low)+(high-low)//2
            if nums[mid]<target:
                low = mid +1
            else:
                high = mid
                
        return low if nums[low]==target else -1 