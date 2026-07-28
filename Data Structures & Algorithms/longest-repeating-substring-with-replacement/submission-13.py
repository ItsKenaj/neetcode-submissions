class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        At first glance this seems like a sliding window problem where we are keeping track
        of the longest window in which we can make replacements s.t. all elements in that window 
        are identical.

        We need to keep track of the frequencies of each char in the window and we choose which character
        we are going to replace with by taking the max of the frequencies


        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        longest_window = 0
        l, r = 0 , 0
        maxF = 0
        freqs = {}

        while r < len(s):
            windowSize = r - l + 1
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            maxF = max(maxF, freqs[s[r]])

            while windowSize - maxF > k:
                freqs[s[l]] -= 1
                l += 1
                windowSize -= 1
            
            longest_window = max(longest_window, windowSize)
            r += 1

        return longest_window
