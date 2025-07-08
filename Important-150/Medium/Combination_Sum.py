class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start: int, subarray: List[int], total: int):
            if total == target:
                res.append(subarray[:])
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                subarray.append(nums[i])
                helper(i, subarray, total + nums[i])  # i instead of i+1 because elements can be reused
                subarray.pop()  # backtrack

        helper(0, [], 0)
        return res

# The below code has also do the same but same child nodes are calling 
# Suppose 2,5,6,9
# Suppose 2 can include 5,6,9 in first iteration 
# Now no need to call 2 in iteration of 5

# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res=[]
#         def helper(subarray):
#             if sum(subarray)==target:
#                 res.append(subarray[:])
#                 return
#             if sum(subarray)>target:
#                 return
#             for ele in nums:
#                 subarray.append(ele)
#                 helper(subarray)
#         helper([])
#         return res

# 🚀 Problem Summary:
# Given: A list of positive integers `nums` and a target sum `target`
# Goal: Return all unique combinations where numbers from `nums` sum to `target`
#        - You can reuse elements multiple times
#        - Combinations should not be repeated in different orders

# 🧩 Brute Force Idea:
# Try all combinations by repeatedly summing elements
# No pruning, tries every path even if it already passed `target`
# Time: O(2^n * k) — exponential due to all subset paths
# Space: O(k) — recursion stack (k = target / min(nums[i]))

# ⚡ Optimization / Pattern Used:
# Pattern: Backtracking with Pruning
# 1. Sort is optional, but helps when you want to add early termination
# 2. Use a helper with:
#     - `start` index → to avoid re-adding smaller elements that have already been considered
#     - `total` → current running sum
#     - `subarray` → current working combination
# 3. Reuse elements by calling `helper(i)` instead of `helper(i+1)`
# Why needed? → Eliminates unnecessary paths and avoids duplicates efficiently

# 🔑 Key Insight:
# The `start` index ensures that elements aren't reconsidered in different order
# Reuse allowed → stay on same index in recursion
# When total exceeds target, stop (prune that path)

# 🧠 Why it works:
# Backtracking explores all valid paths
# Pruning ensures we don’t waste time on invalid sums
# Using `start` instead of `0` removes duplicate sets like [2,2,3] vs [2,3,2]

# 📈 Time & Space Complexity:
# Time: O(2^target) in worst case (heavily input-dependent)
# Space: O(target) for recursion stack

# 📝 My Takeaway:
# This is a textbook backtracking pattern:
#   - Explore → Choose → Backtrack
#   - Add pruning to speed up
# Understanding `start`, `target`, and when to return makes this pattern reusable across:
#   - Combination Sum II (no reuse, skip duplicates)
#   - Combination Sum III (fixed size)
#   - Subsets, permutations, and more
