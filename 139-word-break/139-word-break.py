class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possible = [False]*(len(s)+1)
        possible[0] = True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if possible[i] and s[i:j+1] in wordDict :
                    possible[j+1]=True
        return possible[-1]
                
        