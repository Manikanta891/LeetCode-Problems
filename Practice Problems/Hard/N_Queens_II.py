class Solution:
    def totalNQueens(self, n) :
        res = []

        board = [[0 for _ in range(n)] for _ in range(n)]

        def is_safe(board, row, col):
            # Check vertical column
            for i in range(row):
                if board[i][col] == 1:
                    return False

            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1

            return True

        def solve(row):
            if row == n:
                # Convert board into string representation
                temp = []
                for r in board:
                    temp.append(''.join('Q' if x == 1 else '.' for x in r))
                res.append(temp)
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 1
                    solve(row + 1)
                    board[row][col] = 0  # Backtrack

        solve(0)
        return len(res)

#The logic of this code is similar to the N-Queens problem, but instead of returning the board configurations, it counts the number of valid configurations.