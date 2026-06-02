class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def rotate_corner(r, c):
            top_right = matrix[c][n-1-r]
            matrix[c][n-1-r] = matrix[r][c]

            bottom_right = matrix[n-1-r][n-1-c]
            matrix[n-1-r][n-1-c] = top_right

            bottom_left = matrix[n-1-c][r]
            matrix[n-1-c][r] = bottom_right

            matrix[r][c] = bottom_left

        dim = n
        for i in range(n // 2):
            for j in range(dim - 1):
                rotate_corner(i, i + j)
                print(i, j)
                for row in matrix:
                    print(row)
                print()
            dim -= 2