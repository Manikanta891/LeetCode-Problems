class Solution:
    def subsetsWithDup(self, nums) :
        res=[]
        subarray=[]
        nums.sort()
        def helper(index):
            if index==len(nums):
                res.append(subarray[:])
                return 
            subarray.append(nums[index])
            helper(index+1)
            subarray.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            helper(index+1)
        helper(0)
        return res


# 🚀 Problem Summary:
# Given: A list `nums` that may contain duplicates
# Goal: Return all possible **unique** subsets (the power set)

# 🧩 Brute Force Idea:
# Generate all 2^n subsets using the normal backtracking approach
# Then use a set to remove duplicate subsets
# Time: O(n * 2^n) with overhead of converting to/from tuples
# Space: O(2^n) for storing subsets

# ⚡ Optimization / Pattern Used:
# Pattern: Backtracking + Sorting + Duplicate Skipping
# Step 1: Sort the input → ensures duplicates are adjacent
# Step 2: During backtracking:
#     - Include current element
#     - Exclude duplicates by skipping all next identical elements
# Why needed? → Prevents generating the same subset from different paths

# 🔑 Key Insight:
# After backtracking out (pop), you check if the next index has the same number
# If it does, skip it → avoids reprocessing identical branches in the tree

# 🧠 Why it works:
# Sorting allows us to detect and skip over duplicate values easily
# The skip logic (`while nums[i] == nums[i+1]`) ensures we don’t explore the same subset more than once

# 📈 Time & Space Complexity:
# Time: O(n * 2^n) — still exponential due to all possible subsets
# Space: O(n) — for recursion stack and temporary subset array

# 📝 My Takeaway:
# Handling duplicates is a great test of logic flow in recursion
# The `sort → skip → backtrack` technique is a universal pattern for uniqueness problems
# This pattern shows up in problems like:
#   - Subsets II
#   - Permutations II
#   - Combination Sum II
