class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def dfs(s,ind, buffer,res):
            if ind>4:
                return 
            if ind==4 and not s:
                res.append(buffer[:-1])
                return
            for i in range(1,len(s)+1):
                if s[:i]=="0" or (s[0]!="0" and 0<int(s[:i])<256):
                    dfs(s[i:],ind+1,buffer+s[:i]+".", res)
                              
        dfs(s,0,"", res)
        return res