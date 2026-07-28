class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"

        return encoded

    def decode(self, s: str) -> List[str]:
        ptr = 0
        decoded = []
        while ptr < len(s):
            pound = s.find('#', ptr)
            length = int(s[ptr:pound])
            decoded.append(s[pound+1:pound+1+length])
            ptr = pound + 1 + length

        return decoded 