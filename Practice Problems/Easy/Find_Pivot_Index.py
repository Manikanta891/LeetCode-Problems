class Solution:
    def pivotIndex(arr):
        total = sum(arr)
        left_sum = 0
        middle = 0

        while middle < len(arr):
            right_sum = total - left_sum - arr[middle]
            if left_sum == right_sum:
                return middle
            left_sum += arr[middle]
            middle += 1
        return -1
    
# 🚀 Problem Summary:
# Given: An array `arr` of integers
# Goal: Find the index `i` where the sum of elements to the left of `i` equals the sum of elements to the right of `i`
# If no such index exists, return -1

# 🧩 Brute Force Idea:
# For each index `i`, compute the sum of elements to the left and right
# Compare the two sums and return `i` if they match
# Time: O(n^2) — nested iterations to calculate sums
# Space: O(1)

# ⚡ Optimization / Pattern Used:
# Pattern: Prefix Sum
# Total sum of array is fixed: total = sum(arr)
# At each index:
#   left_sum = sum of elements from 0 to i-1
#   right_sum = total - left_sum - arr[i]
# Compare left_sum and right_sum directly
# Why needed? → Avoids recomputing sums for every index → reduces time to O(n)

# 🔑 Key Insight:
# At pivot index, we must have:
#     left_sum == total - left_sum - arr[i]
# Rearranging avoids repeated right-side summation
# Update left_sum while moving forward through array

# 🧠 Why it works:
# The total sum helps calculate the right sum efficiently in constant time
# We maintain left_sum incrementally, avoiding redundant work

# 📈 Time & Space Complexity:
# Time: O(n) — single pass through array
# Space: O(1) — only variables used, no extra space required

# 📝 My Takeaway:
# Prefix sums are super useful when comparing or computing sections of an array
# Identifying invariants (like total sum) helps optimize brute-force logic