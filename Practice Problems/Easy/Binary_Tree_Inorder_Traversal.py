# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        current = root

        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Visit the node
            current = stack.pop()
            result.append(current.val)

            # Visit the right subtree
            current = current.right

        return result
