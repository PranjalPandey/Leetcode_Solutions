class Solution:
    def binSearch(self, num, ans):
        low,high = 0, len(ans)-1
        mid = (low+high)//2

        while low<=high:
            mid = (low+high)//2
            if ans[mid]==num:
                return mid
            elif ans[mid]>num:
                high = mid-1
            else:
                low =mid+1
        return low
                
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        #using binary search
        ans = []
        ans = [nums[0]]
        for i,num in enumerate(nums):
            if num>ans[-1]:
                ans.append(num)
            else:
                j= self.binSearch(num,ans)
                ans[j]=num
        return len(ans)
        
        