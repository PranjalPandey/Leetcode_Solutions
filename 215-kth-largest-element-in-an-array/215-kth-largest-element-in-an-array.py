import heapq
class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
    
        def add(num):
            heapq.heappush(h,num)
            if len(h)>k:
                heapq.heappop(h)
            
        for num in nums:
            add(num)
        
        return h[0]