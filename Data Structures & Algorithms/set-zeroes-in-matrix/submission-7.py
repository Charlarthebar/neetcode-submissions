class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if isinstance(matrix[r][c], int) and matrix[r][c] == 0:
                    for col in range(cols):
                        if matrix[r][col] != 0:
                            matrix[r][col] = 0,
                    for row in range(rows):
                        if matrix[row][c] != 0:
                            matrix[row][c] = 0,
        for r in range(rows):
            for c in range(cols):
                if isinstance(matrix[r][c], tuple):
                    matrix[r][c] = 0
            