class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_width = len(height)-1
        area = 0
        for width in range(max_width,-1,-1):
            if height[left]<height[right]:
                area = max(area,width*height[left])
                left +=1
            else:
                area = max(area,width*height[right])
                right -=1
        return area
        