class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(p):
                return i == len(s)
            
            firstMatch = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                res = (firstMatch and dfs(i + 1, j)) or dfs(i, j + 2)
            else:
                res = firstMatch and dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return res
            
        
        return dfs(0, 0)
