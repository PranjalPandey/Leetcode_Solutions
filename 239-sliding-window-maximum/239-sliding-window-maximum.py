from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # q = deque()
        # output = []
        # for i in range(len(nums)):
        #     if q and q[0]==i-k:
        #         q.popleft()
        #     while q and nums[q[-1]]<=nums[i]:
        #         q.pop()
        #     q.append(i)
        #     if i>=k-1:
        #         output.append(nums[q[0]])
        # return output
        
        if k==1:
            return nums
        heap =[[-val,ind] for ind,val in enumerate(nums[:k])]
        heapq.heapify(heap)
        res = [-heap[0][0]]
        
        for i in range(k,len(nums)):
            while heap[0][1]<=i-k:
                heapq.heappop(heap)
            heapq.heappush(heap,[-nums[i],i])
            res.append(-heap[0][0])
        return res