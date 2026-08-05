class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word1) + 1)
        prev = [n for n in range(len(word1), -1, -1)]

        for i in range(len(word2) - 1, -1, -1):
            dp[-1] = len(word2) - i
            for j in range(len(word1) - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[j] = prev[j + 1]
                else:
                    dp[j] = 1 + min(dp[j + 1], prev[j + 1], prev[j])
            prev = dp
            dp = [0] * (len(word1) + 1)
        return prev[0]

        
        def dfs(i, j):
            if j == len(word2):
                return 1
            