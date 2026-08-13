class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            row = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box = (r // 3, c // 3)
                if val in row or val in cols[c] or val in boxes[box]:
                    return False
                row.add(val)
                cols[c].add(val)
                boxes[box].add(val)
        return True