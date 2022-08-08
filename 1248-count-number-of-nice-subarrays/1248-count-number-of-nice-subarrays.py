class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd = 0 
        pre = defaultdict(int)
        
        for i in range(len(nums)):
            pre[odd] += 1
            if nums[i]%2 !=0:
                odd+=1
            if odd>=k:
                count += pre[odd-k]
        return count