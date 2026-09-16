class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        zeroSums = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i - 1] == a:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curSum = a + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                
                else:
                    zeroSums.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return zeroSums