
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        ans = []
        for ind,c in enumerate(s):
            if c not in d:
                d[c] = [ind,ind]
            else:
                d[c][1] = ind
        i=0
        max_so_far=0
        start = 0
        while i<len(s):
            if d[s[i]][1] > max_so_far:
                max_so_far = d[s[i]][1]
        
            elif i == max_so_far:
                ans.append(i - start + 1)
                start = i + 1
                max_so_far = i + 1
            
            i+=1
        return ans
        