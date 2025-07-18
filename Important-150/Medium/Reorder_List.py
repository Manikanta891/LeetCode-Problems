# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow.next
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Cut the list at the middle
        slow.next = None

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


# 🚀 Problem Summary:
# Given: Head of a singly linked list
# Goal: Reorder the list in-place as:
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

# 🧩 Brute Force Idea:
# Put all nodes in a list → use two pointers to reorder by alternately picking from front and back
# Time: O(n), Space: O(n)

# ⚡ Optimization / Pattern Used:
# Pattern: Three-Step Linked List Pattern (Find Middle, Reverse, Merge)
# 1️⃣ Find middle using fast & slow pointers
# 2️⃣ Reverse the second half of the list
# 3️⃣ Merge both halves alternately

# 🔑 Key Insight:
# If you can find the middle, then reordering becomes just merging two lists in a zigzag way
# Reversing the second half lets you do the "end-start" style merge

# 🧠 Why it works:
# → Middle splits the list
# → Reverse gives access to last elements in forward traversal
# → Merge simulates the required reorder pattern step by step

# 📈 Time & Space Complexity:
# Time: O(n) — Each step (find middle, reverse, merge) is linear
# Space: O(1) — In-place, no extra data structures used

# 📝 My Takeaway:
# ✅ This is a classic **multi-phase linked list problem**
# ✅ Understand each phase clearly and isolate logic
# ✅ Always handle edge cases: list with 0, 1, or 2 nodes
