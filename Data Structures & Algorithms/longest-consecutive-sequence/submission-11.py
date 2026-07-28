class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortednums = sorted(list(set(nums)))
        if len(sortednums) == 0:
            return 0
        elif len(sortednums) == 1:
            return 1

        longest = 0
        streak = 1
        prev = sortednums[0]
        for i in range(1, len(sortednums)):
            if sortednums[i] == prev + 1:
                streak += 1
            else:
                streak = 1
            
            longest = max(streak, longest)
            prev = sortednums[i]
        
        return longest
            


