from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for ind,c in enumerate(s):
            d[c]+= 1

        for ind,c in enumerate(s):
            if d[c]==1:
                return ind
        return -1
        