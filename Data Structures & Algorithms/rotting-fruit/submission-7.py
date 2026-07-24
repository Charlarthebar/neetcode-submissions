class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh, visited = set(), set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))
        if not fresh:
            return 0
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while q:
            print(time, q)
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            time += 1

        for f in fresh:
            if f not in visited:
                return -1

        return time - 1