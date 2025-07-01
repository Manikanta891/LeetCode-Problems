# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==0:
#             return 1
#         elif n<0:
#             return 0
#         result=self.climbStairs(n-1)+self.climbStairs(n-2)
#         return result

#The below code uses memoization to optimize the recursive solution        
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(k):
            if k == 0:
                return 1
            if k < 0:
                return 0
            if k in memo:
                return memo[k]
            
            memo[k] = dp(k - 1) + dp(k - 2)
            return memo[k]

        return dp(n)

# 🚀 Problem Summary:
# Given: An integer `n` representing the number of stairs
# Goal: Return the number of distinct ways to climb to the top
# Rule: You can climb either 1 or 2 steps at a time

# 🧩 Brute Force Idea:
# Use recursion:
# - At each step, you can take 1 or 2 steps
# - Recurrence relation: ways(n) = ways(n-1) + ways(n-2)
# Base cases:
#   - If n == 0: return 1 (1 way to stay at the ground)
#   - If n < 0: return 0 (no way to reach a negative step)
# Time: O(2^n) — exponential due to repeated subproblems
# Space: O(n) — recursion stack

# ⚡ Optimization / Pattern Used:
# Pattern: Top-Down Dynamic Programming with Memoization
# Store results of subproblems in a dictionary `memo` to avoid recomputation
# Each `dp(k)` is only computed once
# Why needed? → Reduces exponential time to linear time

# 🔑 Key Insight:
# The problem is identical to the Fibonacci sequence:
#   - ways(1) = 1
#   - ways(2) = 2
#   - ways(3) = 3 (1+1+1, 1+2, 2+1)
# You’re just summing two previous results

# 🧠 Why it works:
# The recursive tree has overlapping subproblems (e.g., ways(3) calls ways(2) and ways(1), both called multiple times)
# Memoization ensures each state is solved only once and reused

# 📈 Time & Space Complexity:
# Time: O(n) — each subproblem solved once
# Space: O(n) — for memoization and recursion stack

# 📝 My Takeaway:
# When recursion gets slow due to repeated calls, memoization is the first optimization to try
# Think in terms of states and transitions → classic DP principle
# This is a powerful intro to dynamic programming — helps understand bigger problems like House Robber, Fibonacci, etc.
