class Solution:
    def numDecodings(self, s: str) -> int:
        decodings = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                decodings[i] = 0
            else:
                decodings[i] = decodings[i + 1]
            
            if i + 1 < len(s) and (10 <= int(s[i:i+2]) <= 26):
                decodings[i] += decodings[i + 2]
        return decodings[0]