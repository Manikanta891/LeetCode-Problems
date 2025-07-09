# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         def subsets(index, arr, current, result):
#             if sum(current) == target:
#                 if current not in result:
#                     result.append(current[:])
#                 return
#             elif sum(current)>target or index==len(arr):
#                 return

#             current.append(arr[index])
#             subsets(index + 1, arr, current, result)
#             current.pop()  

#             subsets(index + 1, arr, current, result)
#         result = []
#         if sum(candidates)<target:
#             return result
#         candidates.sort()
#         subsets(0, candidates, [], result)
#         return result
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res


# 🚀 Problem Summary:
# Given: A list `candidates` of integers (may contain duplicates) and a target sum
# Goal: Return all **unique** combinations where numbers sum to target
# Constraint: Each number can be used **only once** (unlike Combination Sum I)

# 🧩 Brute Force Idea:
# Try all subsets using recursion
# Check if sum == target, avoid adding duplicates using list check or sets
# Time: O(2^n * k) due to subset generation and checking duplicates
# Space: O(k) for call stack, O(N) for result set

# ⚡ Optimization / Pattern Used:
# Pattern: Backtracking + Sorting + Duplicate Skipping
# - Sort input first → makes duplicate skipping easier
# - For each index `i`, decide whether to:
#     → Include candidates[i]
#     → Skip it
# - Use a `while` loop to skip duplicates after backtracking
# - Use index `i + 1` to move forward (each element used at most once)
# Why needed? → Guarantees uniqueness and avoids reusing elements

# 🔑 Key Insight:
# Sorting allows you to detect and skip repeated elements in adjacent calls
# Skipping `while candidates[i] == candidates[i+1]` ensures no duplicate paths are formed
# Backtrack cleanly to explore all unique paths without repetition

# 🧠 Why it works:
# It explores all valid combinations using DFS
# Prunes:
#   - If `total > target` → skip that path
#   - If same number is at next index → skip it to avoid duplicate combinations

# 📈 Time & Space Complexity:
# Time: O(2^n) in worst case (exploring all subsets)
# Space: O(n) recursion stack + result space

# 📝 My Takeaway:
# This is a classic variation of Combination Sum:
#   ✅ Combination Sum I → reuse allowed
#   ✅ Combination Sum II → no reuse + skip duplicates
#   ✅ Combination Sum III → fixed count
# The trio of **sort → skip → backtrack** is powerful for all permutation & combination problems
