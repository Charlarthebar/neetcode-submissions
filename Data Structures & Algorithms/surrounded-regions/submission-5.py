class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        m, n = len(board), len(board[0])

        def dfs(r, c, fill):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == "X" or (r, c) in visited:
                return
            visited.add((r, c))
            if fill:
                board[r][c] = "X"
            dfs(r + 1, c, fill)
            dfs(r - 1, c, fill)
            dfs(r, c + 1, fill)
            dfs(r, c - 1, fill)
        
        for r in range(m):
            dfs(r, 0, False)
            dfs(r, n - 1, False)
        for c in range(n):
            dfs(0, c, False)
            dfs(m - 1, c, False)
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                dfs(r, c, True)