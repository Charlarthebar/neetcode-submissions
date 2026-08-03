class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        dp = [0] * (len(text2) + 1)
        prev = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                add = 1 if text1[i] == text2[j] else 0
                dp[j] = max(prev[j], dp[j + 1], prev[j + 1] + add)
            dp, prev = prev, dp
        return prev[0]