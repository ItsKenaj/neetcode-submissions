class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""


        tCounts = {}
        for c in t:
            tCounts[c] = 1 + tCounts.get(c, 0)
        
        sCounts = {}
        needed = len(tCounts)
        satisfied = 0
        minStart = 0
        minLength = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in tCounts:
                sCounts[s[r]] = 1 + sCounts.get(s[r], 0)
                if sCounts[s[r]] == tCounts[s[r]]:
                    satisfied += 1
                
                    while satisfied == needed:
                        while s[l] not in tCounts:
                            l += 1
                        
                        if minLength == 0 or minLength > r - l + 1:
                            minLength = r - l + 1
                            minStart = l
                        
                        sCounts[s[l]] -= 1
                        if sCounts[s[l]] + 1 == tCounts[s[l]]:
                            satisfied -= 1

                        l += 1

            
            r += 1

        if minLength == 0:
            return ""

        return s[minStart: minStart + minLength]
                        

