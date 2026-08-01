class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[-1] = 1

        for i in range(len(coins)):
            for j in range(amount, -1, -1):
                if j + coins[i] <= amount:
                    dp[j] += dp[j + coins[i]]
        return dp[0]