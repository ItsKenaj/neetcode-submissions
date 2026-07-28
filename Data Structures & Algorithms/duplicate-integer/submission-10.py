class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurrences = dict()
        
        for num in nums:
            if occurrences.get(num) is not None:
                return True
            else:
                occurrences[num] = 1
        
        return False
