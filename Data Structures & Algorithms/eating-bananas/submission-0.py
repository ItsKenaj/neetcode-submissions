import math
class Solution:
    def eatTime(self, rate: int, piles: List[int]) -> int:
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / rate)
        
        return total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        answer = upper
        while lower <= upper:
            mid = lower + (upper - lower)//2
            total_time = self.eatTime(mid, piles)
            if total_time <= h:
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1
        
        return ans
