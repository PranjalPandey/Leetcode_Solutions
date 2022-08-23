class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h_count = [0 for i in range(len(citations)+1)]
        # h_index = 0
        # for c in citations:
        #     h_count[min(c,len(citations))]+=1
        # for n in range(len(citations),-1,-1):
        #     h_index +=h_count[n]
        #     if h_index>= n:
        #         return n
        
        return sum(i<j for i,j in enumerate(sorted(citations, reverse= True)))
        