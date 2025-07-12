# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()
#         current = head

#         while current:
#             if current in visited:
#                 return True  # Cycle found

#             visited.add(current)
#             current = current.next

#         return False  # Reached end, no cycle

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         marker = ListNode(99999)  # dummy node as marker

#         current = head
#         while current:
#             if current.next == marker:
#                 return True  # cycle detected

#             next_node = current.next  # store original next
#             current.next = marker     # mark this node as visited
#             current = next_node       # move to next

#         return False  # reached null, no cycle


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # cycle found

        return False  # no cycle


# 🚀 Problem Summary:
# Given: The head of a singly linked list
# Goal: Determine if the list contains a **cycle**

# 🧩 Brute Force Idea:
# Use a set to track visited nodes:
# → Traverse through the list and store references
# → If a node is visited again → cycle exists
# Time: O(n), Space: O(n)

# ⚡ Optimization / Pattern Used:
# Pattern: Floyd's Tortoise and Hare Algorithm
# - Use two pointers (slow and fast)
# - Move slow by 1 step, fast by 2 steps
# - If there’s a cycle, they will eventually meet inside the loop
# - If fast reaches end (null), no cycle

# 🔑 Key Insight:
# In a cycle, a fast pointer will "lap" the slow pointer
# Detecting the meeting point ensures presence of a loop

# 🧠 Why it works:
# If no cycle → fast pointer hits `None`
# If cycle → fast moves around the loop and catches up with slow
# Constant space and guaranteed detection

# 📈 Time & Space Complexity:
# Time: O(n) — at most every node is visited once by each pointer
# Space: O(1) — constant space, no extra data structures

# 📝 My Takeaway:
# This is one of those **must-know pointer tricks**:
#   ✅ Cycle Detection (Floyd’s)
#   ✅ Midpoint of list (fast/slow)
#   ✅ Palindrome Check (slow + reverse second half)
# Practice pointer problems to build strong muscle memory!
