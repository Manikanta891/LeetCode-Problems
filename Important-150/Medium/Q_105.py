# Build Binary Tree from Preorder and Inorder Traversal
# ======================================================
# Given two integer arrays `preorder` and `inorder`, reconstruct the binary tree and return its root.
# Assumes all elements are unique and the tree is a binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Create a hashmap to store value -> index relations for inorder traversal
        # This helps to locate the root index in constant time
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Step 2: Initialize a pointer to track the current index in preorder list
        self.pre_idx = 0

        # Step 3: Define a helper function that builds the tree recursively
        # l and r define the current subtree bounds in the inorder list
        def dfs(l, r):
            # Base case: when left index crosses right, there's no subtree
            if l > r:
                return None

            # Step 4: Get the current root value from preorder and move pointer forward
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # Step 5: Create the root node
            root = TreeNode(root_val)

            # Step 6: Get the index of the root in inorder to divide left and right subtrees
            mid = indices[root_val]

            # Step 7: Recursively build left and right subtrees
            # Elements from l to mid-1 are in the left subtree
            # Elements from mid+1 to r are in the right subtree
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        # Step 8: Start building the tree from the full inorder range
        return dfs(0, len(inorder) - 1)
