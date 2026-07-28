class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        bracket_map = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in bracket_map:
                if stack and stack.pop() == bracket_map[char]:
                    continue
                else:
                    return False
            
            else:
                stack.append(char)

        
        return not stack


