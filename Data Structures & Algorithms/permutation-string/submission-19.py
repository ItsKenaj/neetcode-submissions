class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts, s2_counts = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1
        
        matches = 0
        for i in range(26):
            if s2_counts[i] == s1_counts[i]:
                matches += 1

        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - 97
            s2_counts[idx] += 1
            if s2_counts[idx] == s1_counts[idx]:
                matches += 1
            elif s2_counts[idx] - 1 == s1_counts[idx]:
                matches -= 1

            idx = ord(s2[l]) - 97
            s2_counts[idx] -= 1
            if s2_counts[idx] == s1_counts[idx]: # this decrement in count resulted in the match
                matches += 1
            elif s2_counts[idx] + 1 == s1_counts[idx]: # this decrement in count resulted in the match breaking
                matches -= 1

            l += 1

        return matches == 26