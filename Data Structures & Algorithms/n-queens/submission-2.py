class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def genDiagonals(dim, row, col):
            diags = set()
            for dr in (1, -1):
                for dc in (1, -1):
                    c = 1
                    while 0 <= row + (c * dr) < dim and 0 <= col + (c * dc) < dim:
                        diags.add((row + (c * dr), col + (c * dc)))
                        c += 1
            return diags

        def dfs(board, row, colsUsed, diags1, diags2):
            # print(f'{board} queens:{numQueens}, rows:{rowsUsed}, cols:{colsUsed}, other:{otherUsed}')
            
            if row == n:
                stringBoard = ["".join(r) for r in board]
                res.append(stringBoard)
                return

            # lastRow = board[-1][0] if board else -1
            # lastCol = board[-1][1] if board else -1
            # print(lastRow, lastCol)
            # print()
            for col in range(n):
                if (col in colsUsed or row - col in diags1 or row + col in diags2):
                    continue
                diag1, diag2 = row - col, row + col
                board[row][col] = "Q"
                dfs(board, row + 1, colsUsed | {col}, diags1 | {diag1}, diags2 | {diag2})
                board[row][col] = "."
        
        board = [["."] * n for _ in range(n)]
        dfs(board, 0, set(), set(), set())

        return res