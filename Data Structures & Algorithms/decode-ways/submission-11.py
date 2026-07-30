class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 2)
        dp[-2] = 1
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) == 0:
                continue
            dp[i] = dp[i + 1]
            if int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
        print(dp)
        return dp[0]