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
                if val in row:
                    return False
                row.add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box = (r // 3, c // 3)
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        return True