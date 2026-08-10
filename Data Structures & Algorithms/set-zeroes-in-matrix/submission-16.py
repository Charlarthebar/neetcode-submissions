class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRow = any(v == 0 for v in matrix[0])
        firstCol = False
        for i in range(m):
            firstCol = firstCol or (matrix[i][0] == 0)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        if firstRow:
            for i in range(n):
                matrix[0][i] = 0
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0