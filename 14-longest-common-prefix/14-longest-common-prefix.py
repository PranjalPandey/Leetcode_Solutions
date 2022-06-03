class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        item = strs[0]
        for i,string in  enumerate(strs):
            
            for j,c in enumerate(string):
                if j>=len(item):
                    break
                if item[j]==c:
                    continue
                else:
                    item=item[:j]
                    break
        return item