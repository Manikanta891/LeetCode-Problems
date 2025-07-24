class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 🚀 Problem Summary:
# Given: A Binary Search Tree (BST) and two nodes `p` and `q`.
# Goal: Find the lowest common ancestor (LCA) of the two nodes. The LCA is the lowest node in the tree that has both `p` and `q` as descendants (including itself).

# 🧩 Brute Force Idea:
# - Traverse the entire tree recursively and check if each node is an ancestor of both `p` and `q`.
# - Keep track of all ancestors for both nodes and find the deepest common one.
# - This does not use the BST property, so it's slower: O(n) time, O(n) space.

# ⚡ Optimization / Pattern Used:
# - Utilizes the **Binary Search Tree** property:
#   - All nodes in the left subtree are smaller
#   - All nodes in the right subtree are larger
# - Traverse from the root:
#   - If both nodes are greater than current, go right
#   - If both are smaller, go left
#   - If they split directions or one equals current, current node is the LCA

# 🔑 Key Insight:
# The moment we encounter a node where `p` and `q` are on different sides (or one matches current), we've found the split point — the LCA.

# Edge Cases:
# - If `p` is ancestor of `q` (or vice versa), it will return the ancestor node correctly.
# - Tree is skewed (degenerate BST) — logic still holds.

# 🧠 Why it works:
# Because a BST’s structure narrows down the search efficiently using value comparison.
# We don’t need to visit all nodes — just trace a path from root until the values diverge.

# 📈 Time & Space Complexity:
# Time: O(h), where h is the height of the tree (O(log n) if balanced, O(n) if skewed)
# Space: O(1) since we’re using iteration instead of recursion

# 📝 My Takeaway:
# When dealing with trees and node relationships, always ask: "Can I use structure properties (like BST or heap)?"
# It can drastically reduce time and space complexity.

