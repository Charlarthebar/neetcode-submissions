class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        treasures = set()

        def dfs(distance, r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == -1 or (r, c) in treasures:
                return
            if grid[r][c] == 0:
                treasures.add((r, c))
                dfs(1, r + 1, c)
                dfs(1, r - 1, c)
                dfs(1, r, c + 1)
                dfs(1, r, c - 1)
                return
            
            if distance >= grid[r][c]:
                return
            grid[r][c] = distance
            dfs(distance + 1, r + 1, c)
            dfs(distance + 1, r - 1, c)
            dfs(distance + 1, r, c + 1)
            dfs(distance + 1, r, c - 1)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(0, r, c)