from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = dict(Counter(s))
        flag = True
        count = 0
        while flag:
            flag = False
            for k,v in c.items():
                if v!=0 and v// 2 >= 1:
                    count+=2
                    c[k]-=2
                    flag = True
            
        for k,v in c.items():
            if v!=0 and v%2 !=0 :
                count+=1
                break
        return count
        