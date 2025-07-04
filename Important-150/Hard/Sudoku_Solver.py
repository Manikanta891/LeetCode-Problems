class Solution:
    def solveSudoku(self, board):
        def isValid(r, c, choice, board):
            for i in range(9):
                if board[r][i] == choice:
                    return False
                if board[i][c] == choice:
                    return False

            startRow = 3 * (r // 3)
            startCol = 3 * (c // 3)

            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == choice:
                        return False

            return True

        def fillCell(board):
            for r in range(9):
                for c in range(9):  # ✅ FIXED THIS LINE
                    if board[r][c] == '.':
                        for choice in map(str, range(1, 10)):
                            if isValid(r, c, choice, board):
                                board[r][c] = choice
                                if fillCell(board):
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        fillCell(board)
        

# 🚀 Problem Summary:
# Given: A partially filled 9x9 Sudoku board with empty cells represented as '.'
# Goal: Modify the board in-place to fill in digits (1 to 9) such that the board becomes a valid Sudoku solution

# 🧩 Brute Force Idea:
# Try all numbers (1 to 9) in every empty cell recursively
# For each placement, check if it's valid; if so, move to next cell
# Backtrack if we reach an invalid state
# Time: Extremely high — O(9^(n)) for n empty cells
# Space: O(n) — recursion stack

# ⚡ Optimization / Pattern Used:
# Pattern: Backtracking + Constraint Checking
# At every empty cell:
#   - Try placing digits from 1 to 9
#   - Validate choice (check row, column, and 3x3 box)
#   - If valid, place it and continue recursively
#   - If stuck, undo (backtrack) and try the next digit
# Why needed? → Efficient pruning of invalid paths early

# 🔑 Key Insight:
# Sudoku has strict constraints:
#   - No repetition in rows, columns, or 3x3 subgrids
# By validating choices **before placing**, we drastically reduce invalid search paths

# 🧠 Why it works:
# - Each recursive call solves the board one cell at a time
# - If all cells are filled successfully, the board is solved
# - Backtracking ensures we undo bad decisions and explore other options

# 📈 Time & Space Complexity:
# Time: Worst case is O(9^81) — though pruned heavily with validation
# Space: O(1) for board + O(depth) for recursion stack (~81 max)

# 📝 My Takeaway:
# This is a classic example of constraint-based recursion
# Validity checks (row, col, box) are key to cutting down the search space
# Clean board logic + smart backtracking = powerful problem-solving combo
