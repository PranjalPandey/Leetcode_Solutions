class Solution:
    def longestPalindrome(self, s: str) -> str:
#         ans = ""
#         ansLen = 0
        
#         for i in range(len(s)):
#             l,r = i,i
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if (r-l+1)>ansLen:
#                     ans = s[l:r+1]
#                     ansLen = r-l+1
#                 l-=1
#                 r+=1
            
#             l,r=i,i+1
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if (r-l+1)>ansLen:
#                     ans = s[l:r+1]
#                     ansLen = max(ansLen,(r-l+1))
#                 l-=1
#                 r+=1
#         return ans
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        ans = ""
        
        for d in range(len(s)):
            dp[d][d] = True
            ans = s[d]
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]==True:
                        dp[i][j]=True
                        if len(ans)<len(s[i:j+1]):
                            ans= s[i:j+1]
        return  ans 
            