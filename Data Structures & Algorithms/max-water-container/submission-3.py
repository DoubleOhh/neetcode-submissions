class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1 
        length = j-i
        maxarea = 0 
        
        while i < j:
            mh = min(heights[i],heights[j])
            area = (j-i)*mh
            maxarea = max(maxarea, area)
            length -= 1
            if heights[i] >= heights[j]:
          	    j -=1
            else:
          	    i +=1
        return maxarea