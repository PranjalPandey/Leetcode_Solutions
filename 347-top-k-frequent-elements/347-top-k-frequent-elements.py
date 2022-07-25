from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c= dict(Counter(nums))
        h=[]
        for key,val in c.items():
            h.append((val,key))
        # heapq.heapify(h)
        h.sort(key = lambda x: x[0], reverse = True)
        return [i[1] for i in h[:k]]
        
        