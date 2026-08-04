class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            
            pathLen = 1
            maxPath = 0
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    maxPath = max(maxPath, dfs(nr, nc))
            dp[(r, c)] = pathLen + maxPath
            return dp[(r, c)]
        
        res = 0
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                res = max(res, dfs(r, c))
        print(dp)
        return res