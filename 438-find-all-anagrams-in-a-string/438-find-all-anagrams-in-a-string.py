from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        myDictP=collections.Counter(p)
        myDictS=collections.Counter(s[:len(p)])
        output=[]
        start=0
        end=len(p)

        while end<=len(s):
            if myDictS==myDictP:
                output.append(start)

            myDictS[s[start]]-=1
            if myDictS[s[start]]<=0:
                myDictS.pop(s[start])

            if end<len(s):    
                 myDictS[s[end]]+=1
            end+=1
            start+=1
        return output