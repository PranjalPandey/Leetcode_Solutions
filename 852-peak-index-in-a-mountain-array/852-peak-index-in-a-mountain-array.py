class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #0,1,4,5,6,8,9,10,7,3
        low,high = 0, len(arr)-1
        
        while low<high:
            mid = low +(high-low)//2
            if  arr[mid-1]<=arr[mid] and arr[mid+1]<=arr[mid]:
                return mid
            if arr[mid-1]>=arr[mid]:
                high = mid
            else:
                low = mid
        return low
                