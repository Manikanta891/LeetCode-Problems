class Solution: 
    def solveNQueens(self, n) :
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
        return res


# 🚀 Problem Summary:
# Given: An integer `n`, representing the size of an n x n chessboard
# Goal: Place `n` queens on the board so that no two queens attack each other
# Return all distinct solutions (as a list of board configurations)

# 🧩 Brute Force Idea:
# Try placing queens in all possible positions for each row and column
# Check all permutations and validate board at every step
# Time: Exponential — O(n^n), too slow
# Space: O(n^2) for storing board

# ⚡ Optimization / Pattern Used:
# Pattern: Backtracking
# - Solve one row at a time, trying all columns
# - For each column, check if it’s safe to place a queen (no vertical or diagonal threats)
# - If safe, place the queen and recursively solve for next row
# - If no solution in next rows, **backtrack** by removing the queen
# Why needed? → Prunes large portions of the invalid search space

# 🔑 Key Insight:
# - Only one queen per row is allowed → solve row by row
# - Check safety conditions before placing a queen:
#     - Same column check
#     - Upper-left diagonal
#     - Upper-right diagonal

# 🧠 Why it works:
# Each valid board state gets built incrementally
# If any partial state violates the rules, recursion backtracks early — saving work
# Once we reach `row == n`, we have a valid board → store its string form in result

# 📈 Time & Space Complexity:
# Time: O(n!) — in the worst case, try all column permutations for n rows
# Space: O(n^2) — for storing board + call stack

# 📝 My Takeaway:
# This is a textbook backtracking problem — a must-know for interviews
# Practicing N-Queens teaches how to:
#     - Explore all configurations
#     - Prune invalid ones efficiently
#     - Use recursion and rollback state correctly
