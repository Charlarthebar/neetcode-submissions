class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            p1, p2 = prices[i], prices[i + 1]
            if p2 > p1:
                res += p2 - p1
        return res