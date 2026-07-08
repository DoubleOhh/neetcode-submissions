class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        maxarea = 0
        while l < r and r != l:
            width = r - l
            area = min(heights[r],heights[l]) * width
            maxarea = max(area, maxarea)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxarea