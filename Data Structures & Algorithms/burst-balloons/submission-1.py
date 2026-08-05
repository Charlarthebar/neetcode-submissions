class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(arr):
            if not arr:
                return 0
            tup = tuple(arr)
            if tup in dp:
                return dp[tup]
            
            coins = 0
            for i in range(len(arr)):
                v1 = arr[i - 1] if i - 1 >= 0 else 1
                v2 = arr[i]
                v3 = arr[i + 1] if i + 1 < len(arr) else 1
                cur = dfs(arr[:i] + arr[i + 1:])
                coins = max(coins, cur + v1 * v2 * v3)
            dp[tup] = coins
            return coins

        return dfs(nums)