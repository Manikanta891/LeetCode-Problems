# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        
        # Move first n+1 steps ahead to create the gap
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers
        while first:
            first = first.next
            second = second.next
        
        # Delete the node
        second.next = second.next.next
        
        return dummy.next


# 🚀 Problem Summary:
# Given: A singly linked list and an integer `n`
# Goal: Remove the `n`th node from the end of the list in one pass

# 🧩 Brute Force Idea:
# - Traverse the list to get its length
# - Traverse again to delete (length - n)th node
# Time: O(2n), Space: O(1)

# ⚡ Optimization / Pattern Used:
# Pattern: Two Pointer Technique (Fast & Slow)
# - Move one pointer `n + 1` steps ahead (gap of `n`)
# - Move both until fast pointer reaches the end
# - Now, slow pointer is just before the node to be deleted

# 🔑 Key Insight:
# Using a dummy node before head helps avoid edge case issues like removing the head itself
# Maintaining a gap allows you to delete the node without needing list length

# 🧠 Why it works:
# With `first` ahead by `n + 1`, when `first` hits the end, `second` is at the (n+1)th from the end
# → Exactly what you need to modify `second.next`

# 📈 Time & Space Complexity:
# Time: O(n) — One full pass
# Space: O(1) — Constant extra space

# 📝 My Takeaway:
# ✅ Always use a dummy node to simplify linked list edge cases
# ✅ Perfect demo of fast-slow pointer for positional manipulation
# ✅ This template shows up in many variations — "remove from end", "find middle", "detect cycle", etc.
