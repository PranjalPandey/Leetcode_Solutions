from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        lookup = defaultdict(int)
        counter = 0
        for i,song in enumerate(time):
            if song%60==0:
                counter+=lookup[60]
                lookup[60]+=1
            else:
                counter += lookup[60-song%60]
                lookup[song%60]+=1
        return counter