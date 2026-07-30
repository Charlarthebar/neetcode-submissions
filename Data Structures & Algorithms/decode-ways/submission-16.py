class Solution:
    def numDecodings(self, s: str) -> int:
        first, second = 1, 0

        for i in range(len(s) - 1, -1, -1):
            temp = first
            if s[i] == "0":
                first = 0
            elif int(s[i:i + 2]) <= 26:
                first += second
            second = temp
        return first