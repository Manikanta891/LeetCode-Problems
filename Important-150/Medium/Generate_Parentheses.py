class Solution:
    def generateParenthesis(self, n: int):
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
s1=Solution()
print(s1.generateParenthesis(3))




# 🚀 Problem Summary:
# Given: An integer `n` representing the number of pairs of parentheses
# Goal: Generate all combinations of well-formed parentheses using exactly `n` pairs

# 🧩 Brute Force Idea:
# Generate all 2^(2n) combinations of '(' and ')' characters
# For each combination:

# * Check if it has exactly `n` '(' and `n` ')'
# * Check if it's valid (no prefix has more ')' than '(')
#   Time complexity is O(2^(2n)) for generating, and O(n) to validate each = O(n \* 2^(2n))

# ⚡ Optimization / Pattern Used:
# Pattern: **Backtracking with constraints**
# Instead of generating all, we only build valid strings:

# * Add '(' if count of '(' < `n`
# * Add ')' only if count of ')' < count of '('
#   Why needed? → It prunes invalid strings early and avoids unnecessary recursion

# 🔑 Key Insight:
# Only generate valid prefixes — never allow more ')' than '(' while building
# This avoids building wrong branches in recursion

# 🧠 Why it works:
# The recursion tree only explores valid moves (like a balanced binary tree path)
# Every full-length path (2n) that satisfies constraints is a valid answer

# 📈 Time & Space Complexity:
# Time: O(2^n \* n) — Catalan number growth, where `n` is the number of pairs
# Space: O(n) recursion stack + O(number of valid combinations)

# 📝 My Takeaway:
# Brute force wastes time generating invalid sequences
# Backtracking shines here by building smart and pruning early
# Understanding constraints and applying them during construction saves a TON of effort
