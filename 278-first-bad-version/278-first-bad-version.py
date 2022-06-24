# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid= (low)+(high-low)//2
        while low<high:
            mid= (low)+(high-low)//2
            if isBadVersion(mid)==False:
                low=mid+1
            else:
                high=mid
        return low
                
                
                
        