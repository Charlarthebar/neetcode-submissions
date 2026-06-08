class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)], [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
        boxes = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    digit = int(board[r][c]) - 1
                    rows[r][digit] += 1
                    cols[c][digit] += 1
                    boxNum = ((r // 3) * 3) + (c // 3)
                    boxes[boxNum][digit] += 1
        
        for row in rows:
            if any(val > 1 for val in row):
                return False
        for col in cols:
            if any(val > 1 for val in col):
                return False
        for box in boxes:
            if any(val > 1 for val in box):
                return False
        return True