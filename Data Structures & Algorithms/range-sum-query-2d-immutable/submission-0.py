class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.sums[r][c] = self.sums[r - 1][c] + self.sums[r][c - 1] - self.sums[r - 1][c - 1] + matrix[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1 
        col2 += 1

        trRow, trCol = row1, col2
        blRow, blCol = row2, col1

        return self.sums[row2][col2] - self.sums[trRow - 1][trCol] - self.sums[blRow][blCol - 1] + self.sums[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)