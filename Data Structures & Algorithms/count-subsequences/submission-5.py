class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(int)

        def dfs(p1, p2):
            if p2 == len(t):
                return 1
            if p1 == len(s):
                return 0
            if (p1, p2) in dp:
                return dp[(p1, p2)]
            
            res = 0
            if s[p1] == t[p2]:
                res += dfs(p1 + 1, p2 + 1)
            res += dfs(p1 + 1, p2)
            dp[(p1, p2)] = res
            return dp[(p1, p2)]
        
        return dfs(0, 0)