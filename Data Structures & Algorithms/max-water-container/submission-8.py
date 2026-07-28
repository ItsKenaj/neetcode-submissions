class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_area = 0
        while l < r:
            if heights[l] <= heights[r]:
                max_area = max(max_area, (r - l) * heights[l])
                l += 1
            else:
                max_area = max(max_area, (r - l) * heights[r])
                r -= 1
        
        return max_area
            