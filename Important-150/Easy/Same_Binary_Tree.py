class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



# 🚀 Problem Summary:
# Given: Two binary trees, `p` and `q`.
# Goal: Determine if the trees are structurally identical and the nodes have the same values.

# 🧩 Brute Force Idea:
# Compare every node of both trees using recursion.
# For each node, compare:
# - If both nodes are None → OK
# - If one is None and the other isn’t → Not same
# - If both exist but values differ → Not same
# - Otherwise, recursively check left and right subtrees
# Time complexity is still optimal here as there's no obvious brute vs optimized split.

# ⚡ Optimization / Pattern Used:
# Pattern: Recursion with early termination
# Why needed: Because binary trees can vary in depth/structure,
# recursion allows dynamic depth traversal.
# Early return prevents unnecessary work as soon as we find a mismatch.

# 🔑 Key Insight:
# If at any point one node is None and the other isn’t — or values don’t match — the trees differ.
# If both nodes are None, that subtree is identical.
# Otherwise, check left and right subtrees recursively.

# 📦 Edge Cases:
# - Both trees are empty (None) → True
# - One tree empty, one not → False
# - Values same but structure different → False

# 🧠 Why it works:
# Because the recursion checks every node in sync for value and structure,
# and exits early if a difference is found.
# Think of it like a parallel preorder traversal.

# 📈 Time & Space Complexity:
# Time: O(n), where n is the number of nodes in the smaller tree (worst case: both are same size)
# Space: O(h), where h is the height of the tree (due to recursion stack)

# 📝 My Takeaway:
# Recursion simplifies problems with unknown depth/size like trees.
# Checking structure and value in sync avoids missing subtle mismatches.
# This is a foundational tree problem every CSE student should master!


