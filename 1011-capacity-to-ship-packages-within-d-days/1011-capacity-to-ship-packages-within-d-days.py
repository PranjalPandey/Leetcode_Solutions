class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(limit):
            total = 0
            count = 1
            for w in weights:
                total+=w
                if total>limit:
                    total = w
                    count+=1
                    if count>days:
                        return False
            return True
            
        low = max(weights)
        high = sum(weights)
        while low<high:
            mid =  (low)+(high-low)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low