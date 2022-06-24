class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        if x==0:
            return 0
        if x==1:
            return 1
        while low<high:
            mid = (low)+(high-low)//2
            if mid*mid<=x:
                low = mid+1
            else:
                high = mid
        return low-1
            
        