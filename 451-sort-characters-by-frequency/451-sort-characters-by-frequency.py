from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = dict(Counter(s))
        ans = ''
        for k,v in sorted(list(c.items()),key = lambda x:x[1], reverse = True):
            for i in range(v):
                ans +=k
            
        return ans