class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area

        for row in range(rows):
            for col in range(cols):
                area = dfs(row, col)
                print(area)
                res = max(res, area)
        return res