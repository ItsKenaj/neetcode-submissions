from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1
               
        for key in s_dict.keys():
            if t_dict[key] != s_dict[key]:
                return False
        
        return True