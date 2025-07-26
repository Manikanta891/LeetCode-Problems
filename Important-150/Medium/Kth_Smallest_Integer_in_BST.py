# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         data=[]
#         def helper(root):
#             if root is None:
#                 return
#             helper(root.left)
#             data.append(root.val)
#             helper(root.right)
#         helper(root)
#         return data[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result


# 🚀 Problem Summary:
# Given: A Binary Search Tree (BST) and an integer k
# Goal: Find the k-th smallest element in the BST.

# 🧩 Brute Force Idea:
# - Perform in-order traversal to collect all elements in a list.
# - In-order traversal of BST gives elements in sorted order.
# - Return k-1 index from list.
# - Time: O(n), Space: O(n)

# ⚡ Optimized Version:
# - Use in-order traversal but stop as soon as we reach the k-th node.
# - Avoid storing all nodes — reduce space to O(1) (ignoring recursion stack).

# 🔑 Key Insight:
# In-order traversal of BST gives nodes in ascending order.
# So just count while traversing and return the k-th visited node.

# Edge Cases:
# - k = 1 (smallest element)
# - k = number of nodes (largest element)

# 📈 Time & Space Complexity:
# Time: O(k) in best case, O(n) in worst if k == n
# Space: O(h) recursion stack (h = height of tree)

# 📝 My Takeaway:
# Optimize space in traversal-based questions by directly acting on counts.
# Track early exits from recursion to save extra work.
