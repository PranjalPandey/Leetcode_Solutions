class Solution:
    def reverseBits(self, n: int) -> int:
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
        
        
        