# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev


# 🚀 Problem Summary:
# Given: The head of a singly linked list
# Goal: Reverse the linked list and return the new head

# 🧩 Brute Force Idea:
# Not applicable directly — can't brute force this meaningfully without modifying the structure
# But one inefficient way: Copy nodes to an array, reverse it, and reconstruct the list
# Time: O(n), Space: O(n) — not ideal

# ⚡ Optimization / Pattern Used:
# Pattern: Iterative pointer reversal
# Use 3 pointers — `prev`, `curr`, `next_node`
# Reverse the `.next` pointer of each node to point backward
# Why needed? → Reverses the list in-place using constant space

# 🔑 Key Insight:
# Carefully update pointers in a single pass:
# - Save `next_node` before breaking link
# - Reverse `curr.next` to point to `prev`
# - Move `prev` and `curr` one step forward

# 🧠 Why it works:
# We traverse the list once, at each step reversing the link direction
# By the end, `prev` points to the new head (last node of the original list)

# 📈 Time & Space Complexity:
# Time: O(n) — each node visited once
# Space: O(1) — in-place reversal, no extra space used

# 📝 My Takeaway:
# Reversing a list is a pointer manipulation problem — get the order of updates right
# Practicing with a dry run on paper really helps solidify the logic
# Recursive approach is also elegant but uses more space
