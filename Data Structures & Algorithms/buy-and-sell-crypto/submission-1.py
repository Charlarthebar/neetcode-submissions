class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i = 0
        j = 1
        while i < len(prices)-1 and j < len(prices):
            n = prices[i]
            comp = prices[j]
            if n < comp:
                m = max(m, comp - n)    
            elif n > comp:
                i = j
            j += 1
        return m
