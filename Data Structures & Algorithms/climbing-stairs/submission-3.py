class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dp(num):
            print(num)
            if num == 1:
                memo[n] = 1
                return 1
            if num == 2:
                memo[num] = 2
                return 2
            if memo[num] != -1:
                return memo[num]
            res = dp(num - 2) + dp(num - 1)
            memo[num] = res
            return res
        return dp(n)