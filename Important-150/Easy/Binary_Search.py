class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while high>=low:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1
    
# 🚀 Problem Summary:
# Given: A sorted list `nums` and a target integer `target`
# Goal: Return the index of `target` in `nums` using binary search, or -1 if not found

# 🧩 Brute Force Idea:
# Iterate through the array and compare each element with the target
# If match found, return the index
# Time: O(n) — linear search
# Space: O(1)

# ⚡ Optimization / Pattern Used:
# Pattern: Binary Search
# We divide the search space in half each time
# Why needed? → The array is sorted, so binary search gives O(log n) efficiency over O(n)

# 🔑 Key Insight:
# Calculate `mid` = (low + high) // 2
# - If `nums[mid] == target`, return `mid`
# - If `target < nums[mid]`, discard right half (high = mid - 1)
# - Else discard left half (low = mid + 1)

# 🧠 Why it works:
# Every iteration halves the search space
# This leads to logarithmic time complexity and ensures efficient lookup in sorted data

# 📈 Time & Space Complexity:
# Time: O(log n) — search space is halved each step
# Space: O(1) — uses constant extra space

# 📝 My Takeaway:
# Binary Search is a go-to technique for any problem involving sorted data
# Make sure to understand edge handling (like off-by-one in low/high)
# Clean implementation like this is a must-know for interviews
