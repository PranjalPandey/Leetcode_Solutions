class Solution:
    def squared(self, n):
        return sum([int(i)**2 for i in str(n)])
        
    def isHappy(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(self.squared(n))
        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
        return fast==1


                
            