class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            new = dp[:]
            for j in range(len(text2) - 1, -1, -1):
                add = 1 if text1[i] == text2[j] else 0
                new[j] = max(dp[j], new[j + 1], dp[j + 1] + add)
            dp = new
        return dp[0]