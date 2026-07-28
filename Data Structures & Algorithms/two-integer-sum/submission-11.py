class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        want = target
        for i in range(len(nums)):
            want -= nums[i]
            for j in range(i+1, len(nums)):
                if want == nums[j]:
                    return [i, j]
            
            want += nums[i]
        
        return []


