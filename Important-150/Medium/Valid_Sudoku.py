class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            row_set = set()
            col_set = set()
            box_set = set()
            for j in range(9):
                # Row check
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                
                # Column check
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
                
                # Box check (i // 3)*3 gives starting row, i % 3 gives column offset
                row = 3 * (i // 3) + (j // 3)
                col = 3 * (i % 3) + (j % 3)
                if board[row][col] != '.':
                    if board[row][col] in box_set:
                        return False
                    box_set.add(board[row][col])
        return True



# 🚀 Problem Summary:
# Given: A 9x9 Sudoku board (partially filled) where empty cells are denoted by '.'
# Goal: Check if the current configuration is valid according to Sudoku rules:
# - Each row must have unique digits 1–9
# - Each column must have unique digits 1–9
# - Each 3x3 sub-box must have unique digits 1–9

# 🧩 Brute Force Idea:
# Use three separate checks:
# - For every row, scan and store digits seen
# - For every column, scan and store digits seen
# - For each of the 9 sub-boxes, check for duplicates
# Time: Still O(1) since board size is fixed (9x9)
# Space: Can be optimized but clear with sets

# ⚡ Optimization / Pattern Used:
# Pattern: Set-based uniqueness check
# Loop through each row index `i` from 0 to 8
# - In each iteration, maintain three sets: row_set, col_set, box_set
# - For `j` from 0 to 8:
#     - Validate row: board[i][j]
#     - Validate column: board[j][i]
#     - Validate 3x3 box using:
#         row = 3 * (i // 3) + (j // 3)
#         col = 3 * (i % 3) + (j % 3)
# Why needed? → Simultaneous validation in a single loop per index

# 🔑 Key Insight:
# Index math helps us map any sub-box into linear iteration
# `(i // 3) * 3 + (j // 3)` and `(i % 3) * 3 + (j % 3)` are gold for 3x3 navigation

# 🧠 Why it works:
# Every digit is checked only once per rule (row, column, box)
# Sets naturally prevent duplicates, and allow fast lookups
# Runs efficiently even though it loops a fixed number of times

# 📈 Time & Space Complexity:
# Time: O(1) — board is always 9x9, so 81 cells max
# Space: O(1) — up to 3 sets of size ≤9 per iteration

# 📝 My Takeaway:
# This is a brilliant example of combining index tricks with set logic
# Index formulas for sub-boxes are the hardest part — once understood, the rest is clean
# Great example of validating multiple constraints in a single pass
