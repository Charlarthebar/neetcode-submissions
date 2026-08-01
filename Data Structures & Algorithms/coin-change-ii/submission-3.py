class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if total == amount:
                dp[(i, total)] += 1
                return dp[(i, total)]
            if i == len(coins) or total > amount:
                return 0
            
            res = dfs(i, total + coins[i]) + dfs(i + 1, total)
            dp[(i, total)] = res
            return res
        return dfs(0, 0)