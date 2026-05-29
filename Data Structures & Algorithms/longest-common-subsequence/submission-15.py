class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        original_text2 = text2

        for row in range(rows):
            for col in range(cols):
                c1 = dp[row-1][col] if row - 1 >= 0 else 0
                c2 = dp[row][col - 1] if col - 1 >= 0 else 0
                c3 = dp[row - 1][col - 1] if row - 1 >= 0 and col - 1 >= 0 else 0

                if text1[row] == text2[col]:
                    dp[row][col] = c3 + 1
                else:
                    dp[row][col] = max(c1, c2)
        return dp[rows-1][cols-1]
                