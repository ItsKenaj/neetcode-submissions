class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        longest = 0

        unique = set()
        count = 0
        while r < len(s):
            if s[r] in unique:
                unique.remove(s[l])
                l += 1
                count -= 1
            else:
                unique.add(s[r])
                count += 1
                longest = max(longest, count)
                r += 1
            

        return longest



