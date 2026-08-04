class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(s) + 1)
        prev = [1] * (len(s) + 1)

        for i in range(len(t) - 1, -1, -1):
            print(dp)
            print(prev)
            print()
            for j in range(len(s) - 1, -1, -1):
                dp[j] = dp[j + 1]
                dp[j] += prev[j + 1] if s[j] == t[i] else 0
                print(i, j, s[j], t[i])
            prev = dp
            dp = [0] * (len(s) + 1)

        print(dp)
        print(prev)
        return prev[0]