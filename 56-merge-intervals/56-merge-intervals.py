class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][0] = min(intervals[i][0],intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i+=1
        return intervals