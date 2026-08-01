class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                res = max(-prices[i] + dfs(i + 1, False), dfs(i + 1, True))
            else:
                res = max(prices[i] + dfs(i + 2, True), dfs(i + 1, False))
            dp[(i, buying)] = res
            return res
        return dfs(0, True)
