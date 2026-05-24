class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(board)
        cols = len(board[0])

        def helper(start, visited, word):
            if not word:
                return True
            for direction in dirs:
                pot_x = start[0] + direction[0]
                pot_y = start[1] + direction[1]
                if (pot_x, pot_y) in visited or pot_x < 0 or pot_x > len(board) - 1 or pot_y < 0 or pot_y > len(board[0]) - 1:
                    continue
                if board[pot_x][pot_y] == word[0]:
                    visited.add((pot_x, pot_y))
                    if helper((pot_x, pot_y), visited, word[1:]):
                        return True
                    visited.remove((pot_x, pot_y))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if helper((i, j), {(i, j)}, word[1:]):
                        return True
        
        return False