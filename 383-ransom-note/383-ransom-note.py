from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = dict(Counter(ransomNote))
        c2 = dict(Counter(magazine))
        for k,v in c1.items():
            if (k not in c2) or (v>c2[k]):
                return False
        return True