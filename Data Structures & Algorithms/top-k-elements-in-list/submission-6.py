from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        sorted_keys_desc = sorted(freqs, key=freqs.get, reverse=True)
        return sorted_keys_desc[:k]
            