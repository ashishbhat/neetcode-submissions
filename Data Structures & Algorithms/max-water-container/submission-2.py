class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_water = 0

        while l < r:
            if heights[l] <= heights[r]:
                max_water = max(max_water, (r-l)*heights[l])
                l += 1
            else:
                max_water = max(max_water, (r-l)*heights[r])
                r -= 1
        return max_water

        