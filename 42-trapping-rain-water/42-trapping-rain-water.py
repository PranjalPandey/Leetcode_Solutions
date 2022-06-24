class Solution:
    def trap(self, heights: List[int]) -> int:
        lmax = [0 for i in range(len(heights))]
        rmax = [0 for i in range(len(heights))]
        lm=0
        rm=0
        summ = 0
        for h,height in enumerate(heights):
            lmax[h]=max(lm,height)
            lm = max(lm,height)
        for h,height in reversed(list(enumerate(heights))):
            rmax[h]=max(rm,height)
            rm = max(rm,height)
        for h, height in enumerate(heights):
            summ+=min(lmax[h],rmax[h])-height
        return summ
        