class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict(Counter(s))
        ans = ""
        h = []
        for k in d.keys():
            heapq.heappush(h,(-d[k],k))
        while len(h)>1:
            f1,c1 = heapq.heappop(h)
            f2,c2 = heapq.heappop(h)

            ans+=c1+c2
            if abs(f1)>1:
                heapq.heappush(h,(f1+1,c1))
            if abs(f2)>1:
                heapq.heappush(h,(f2+1,c2))

        if h:
            f,c = heapq.heappop(h)
            if abs(f)>1:
                return ""
            else:
                ans+=c
        return ans