class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1

        water = 0
        while l <= r:
            if min(maxL, maxR) == maxL:
                water += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                water += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1
        
        return water
