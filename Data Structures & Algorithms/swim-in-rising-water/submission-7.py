class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        def genNeighbors(r, c):
            neighbors = []
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    neighbors.append((nr, nc))
            return neighbors

        heap = [(grid[0][0], (0, 0))] # grid value, coord
        visited = {(0, 0)}
        while heap:
            time, coord = heapq.heappop(heap)
            r, c = coord
            if r == n - 1 and c == n - 1:
                return time
            for nr, nc in genNeighbors(r, c):
                if (nr, nc) not in visited:
                    heapq.heappush(heap, (max(time, grid[nr][nc]), (nr, nc)))
                    visited.add((nr, nc))