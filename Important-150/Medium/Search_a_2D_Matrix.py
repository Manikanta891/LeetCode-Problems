class Solution:
    def searchMatrix(self, matrix, target):
        row=0
        for i in range(len(matrix)):
            if matrix[i][-1]==target:
                return True
            elif matrix[i][-1]>target:
                row=i
                break
        for i in range(len(matrix[row])):
            if matrix[row][i]==target:
                return True
        return False
    

# 🚀 Problem Summary:
# Given: A 2D matrix where:
#   - Each row is sorted left to right
#   - The first integer of each row is greater than the last integer of the previous row
# Goal: Determine if the target exists in the matrix

# 🧩 Brute Force Idea:
# Check every element in the matrix with nested loops
# Time: O(m * n), Space: O(1)
# Not efficient for large matrices

# ⚡ Optimization / Pattern Used:
# Pattern: Two-Phase Linear Search (Row Reduction + Row Scan)
# 1. Find the row where `target` could be present (last element of the row ≥ target)
# 2. Perform a linear search in that specific row
# Why needed? → Reduces unnecessary scanning of unrelated rows

# 🔑 Key Insight:
# Because each row's last element is the upper bound for that row,
# we can skip rows where `matrix[i][-1] < target`

# 🧠 Why it works:
# Rows are strictly increasing overall, so if the last element of a row is less than target,
# the entire row can be skipped. Once the row is found, linear scan is safe.

# 📈 Time & Space Complexity:
# Time: O(m + n) in worst case — O(m) to locate row + O(n) to scan that row
# Space: O(1) — constant space used

# 📝 My Takeaway:
# While this approach is good, we can do even better:
# Treat the matrix as a flat sorted array and apply binary search → O(log(m * n))
# Still, this logic is great when clarity matters over raw speed
