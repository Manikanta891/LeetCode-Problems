# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         def helper(root):
#             if root is None:
#                 return True
#             l=r=True
#             if root.left:
#                 if root.val>root.left.val:
#                     l=helper(root.left)
#                 else:
#                     l=False
#             if root.right:
#                 if root.right.val>root.val:
#                     r=helper(root.right)
#                 else:
#                     r=False
#             return l and r
#         return helper(root)
            
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, float('-inf'), float('inf'))


# ✅ Problem: Validate Binary Search Tree
# Goal: Check whether a given binary tree is a valid BST.
# A BST must satisfy: left < root < right for every subtree

# 🔍 Initial Attempt (Incorrect in Some Cases):
# This version only compares current node with immediate children,
# but doesn't enforce full subtree constraints.
# For example, it allows a left-right grandchild greater than root, which violates BST.

# ✅ Optimized & Correct Approach:
# 🔄 Use DFS with valid value range (low, high) for each node.
# - All node values must lie strictly within the current (low, high) range.
# - Left subtree: range becomes (low, node.val)
# - Right subtree: range becomes (node.val, high)

# 🧠 Why this works:
# It ensures the entire subtree follows the BST rule, not just immediate children.

# 📈 Time: O(n), Space: O(h)
# Where n = number of nodes, h = height of the tree
