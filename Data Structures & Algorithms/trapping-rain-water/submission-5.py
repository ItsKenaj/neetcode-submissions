class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        curMax = 0
        for i in range(n):
            leftMax[i] = curMax
            curMax = max(curMax, height[i])
        
        curMax = 0
        rightMax = [0] * n
        for i in range(n - 1, -1, -1):
            rightMax[i] = curMax
            curMax = max(curMax, height[i])

        trapped = 0
        for i in range(n):
            trapped += max(0, min(leftMax[i], rightMax[i]) - height[i])

        return trapped