class Solution:
    def numDecodings(self, s: str) -> int:
        # count = 1

        # for i in range(len(s)):
        #     if s[i] == "0":
        #         return 0
        #     if int(s[i: i+2]) <= 26:
        #         count += 1
        # return count
        
        memo = {}
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]

            count = dp(i + 1)

            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                count += dp(i + 2)
            memo[i] = count
            return count
        return dp(0)

        # def dp(i):
        #     nonlocal count
        #     if i >= len(s) - 1:
        #         if i == len(s) - 1 and s[i] == "0":
        #             return
        #         count += 1
        #         return
        #     if s[i] == "0":
        #         return 

        #     dp(i + 1)

        #     if int(s[i:i+2]) > 26:
        #         return

        #     dp(i + 2)
        # dp(0)
        # return count
