# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         found=False
#         def helper(index):
#             nonlocal found
#             if index==len(nums)-1:
#                 found=True
#                 return 
#             if index>=len(nums):
#                 return 
#             i=1
#             while i<=nums[index]:
#                 helper(index+i)
#                 i+=1
#         helper(0)
#         return found
#The above problem will find out solution in all possible ways so time complexcity is more


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            if max_reach==len(nums)-1:
                return True
            max_reach = max(max_reach, i + nums[i])
        return True

# 🚀 Problem Summary:
# Given: An array `nums` where each element represents the max jump length at that index
# Goal: Determine if you can reach the last index starting from index 0

# 🧩 Brute Force Idea:
# Try all possible jump paths using recursion
# At each index, try every jump from 1 to nums[index]
# Base case: if you reach the last index, return True
# Time: O(2^n) — exponential due to overlapping subproblems
# Space: O(n) — recursion stack
# Not scalable

# ⚡ Optimization / Pattern Used:
# Pattern: Greedy Forward Scan
# - Track `max_reach`: the farthest index reachable so far
# - At every index `i`:
#     - If `i > max_reach`, then you’re stuck → return False
#     - Else, update max_reach = max(max_reach, i + nums[i])
# - If at any point `max_reach >= last index`, return True
# Why needed? → Eliminates the need to explore all paths — just keep moving as far as possible

# 🔑 Key Insight:
# If you ever hit a position where your current index is greater than `max_reach`, you’re stuck
# Otherwise, greedily expand your reach and continue

# 🧠 Why it works:
# You only need to know **whether** you can reach the end — not how
# So maximize your reach at each step and bail out early if stuck

# 📈 Time & Space Complexity:
# Time: O(n) — single pass through the array
# Space: O(1) — only a few variables used

# 📝 My Takeaway:
# This is one of the most elegant greedy problems — reach as far as you can
# A key pattern: "maximum reach while scanning forward" shows up in many greedy Qs (e.g., Jump Game II, Gas Station)
# Always think: “What is the furthest I can go from here?” — not “What are all the paths I can take?”
