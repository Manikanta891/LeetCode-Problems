class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# 🚀 Problem Summary:
# Given: A binary tree
# Goal: Determine if the tree is height-balanced, i.e., for every node,
#       the height difference between left and right subtrees is no more than 1.

# 🧩 Brute Force Idea:
# For each node, recursively calculate the height of its left and right subtree.
# Then check if their height difference is > 1. Recalculate height every time.
# Time Complexity: O(n^2) in worst case due to repeated height calculations.

# ⚡ Optimization / Pattern Used:
# Use DFS (post-order traversal) to compute height and balance info in one pass.
# The trick is to return a tuple (isBalanced, height) for each subtree.
# This avoids redundant height calculations and stops early when imbalance is found.

# 🔑 Key Insight:
# You can avoid recomputing height multiple times by passing height along with balance status.
# If any subtree is unbalanced, we don't proceed deeper into that branch.

# 🧠 Why it works:
# Post-order traversal ensures we first solve the children and use their results.
# Combining balance check and height in one recursion makes it efficient and early-stopping.

# 📈 Time & Space Complexity:
# Time: O(n) - every node is visited once
# Space: O(h) - height of the recursion stack, worst case O(n) for skewed tree

# 🗒 My Takeaway:
# Smart use of recursion can turn a brute-force approach into an optimized solution.
# This pattern of returning extra state (like height) from recursion is reusable in many tree problems.


