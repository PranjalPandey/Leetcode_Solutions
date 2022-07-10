class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = dict(Counter(words))
        # hp = [(val,key) for key,val in c.items()]
        # hp.sort(key=lambda k: (-k[0], k[1]))
        # return [item[1] for item in hp][:k]
        hp = [[-val,key] for key,val in c.items()]
        heapq.heapify(hp)
        return ([heapq.heappop(hp)[1] for _ in range(k)])
