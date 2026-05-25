class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, prev_height, visited):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev_height:
                return 
            
            visited.add((r, c))
            cur_height = heights[r][c]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, cur_height, visited)
            return

        for r in range(rows):
            dfs(r, 0, float('-inf'), pacific)
            dfs(r, cols - 1, float('-inf'), atlantic)
        for c in range(cols):
            dfs(0, c, float('-inf'), pacific)
            dfs(rows - 1, c, float('-inf'), atlantic)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        return res