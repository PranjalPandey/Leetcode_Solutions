class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(limit):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total>limit:
                    total = num
                    count+=1
                    if count>m:
                        return False
            return True
        low,high = max(nums), sum(nums)
        while low<high:
            mid = (low)+(high-low)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low
            
                