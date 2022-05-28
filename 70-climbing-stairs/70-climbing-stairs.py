class Solution:
    def climbStairs(self, A: int) -> int:
        #Using bottom up approach
        ways=[0]*(A+1)
        ways[0]=1
        ways[1]=1
        i=2
        if A==0 or A==1:
            return 1
        while i<=A:
            ways[i]=ways[i-1]+ways[i-2]
            i+=1
        return ways[A]