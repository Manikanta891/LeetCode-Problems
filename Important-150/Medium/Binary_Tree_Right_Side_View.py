# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node, depth, max_reached):
            if not node:
                return max_reached
            if depth > max_reached:
                res.append(node.val)
                max_reached = depth
            max_reached = helper(node.right, depth + 1, max_reached)
            max_reached = helper(node.left, depth + 1, max_reached)
            return max_reached
        helper(root, 0, -1)
        return res




# 🌳 Problem: Binary Tree Right Side View
# Goal: Return the values of the nodes visible from the right side of the binary tree (top to bottom).

# 🧠 Key Idea:
# At each depth, only the **rightmost** node should be visible.
# We use DFS (Depth-First Search) and prioritize visiting the right subtree first.
# Keep track of the current depth, and when you first reach a new depth, add the node to the result.

# ✅ Why This Works:
# Since we go right before left, the first node we encounter at each depth is the rightmost node.
# By tracking the deepest level reached so far, we ensure we only add one node per depth.

# 📦 Algorithm:
# 1. Use a helper function to traverse the tree.
# 2. Track current `depth` and `max_reached` depth so far.
# 3. If current depth > max_reached, add node to result.
# 4. Traverse right subtree first, then left.

# ⏱ Time Complexity: O(n) — every node is visited once.
# 🧠 Space Complexity: O(h) — recursion stack space (h = height of tree).
