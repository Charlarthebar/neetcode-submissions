class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        atlantic, pacific = set(), set()

        def dfs(r, c, visited, prev):
            if r < 0 or r == m or c < 0 or c == n or (r, c) in visited or heights[r][c] < prev:
                return
            visited.add((r, c))
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, float('-inf'))
                if r == m - 1 or c == n - 1:
                    dfs(r, c, atlantic, float('-inf'))

        res = []
        for coord in atlantic:
            if coord in pacific:
                res.append([coord[0], coord[1]])
        return res