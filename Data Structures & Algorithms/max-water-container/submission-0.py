class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        n = len(heights)
        left,right = 0, n -1

        while left < right:
            area = (right - left) * min(heights[left],heights[right])
            maxWater = max(area,maxWater)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater            
