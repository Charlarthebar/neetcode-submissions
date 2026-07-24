class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, d = queue.popleft()
            grid[r][c] = min(grid[r][c], d)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == -1 or grid[nr][nc] == 0 or d >= grid[nr][nc]:
                    continue
                queue.append((nr, nc, d + 1))
