class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            midRow, midCol = ((l + r) // 2) // cols, ((l + r) // 2) % cols
            if matrix[midRow][midCol] > target:
                r = midRow * cols + midCol - 1
            elif matrix[midRow][midCol] < target:
                l = midRow * cols + midCol + 1
            else:
                return True
        return False
            