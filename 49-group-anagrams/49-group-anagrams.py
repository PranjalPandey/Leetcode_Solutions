from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i,w in enumerate(strs):
            d[tuple(sorted(list(Counter(w).items())))].append(i)
        for i in d.values():
            for j in range(len(i)):
                i[j]=strs[i[j]]


        return sorted(d.values())
