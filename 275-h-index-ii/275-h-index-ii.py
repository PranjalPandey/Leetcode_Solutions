class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i<j for i,j in enumerate(citations[::-1]))