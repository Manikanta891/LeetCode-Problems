# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# 🚀 Problem Summary:
# Given: Two non-empty linked lists representing two non-negative integers (reversed order)
# Goal: Return a linked list representing the sum of the two numbers (also in reversed order)

# 🧩 Brute Force Idea:
# - Convert both lists into numbers → add them → convert result back into a linked list
# - Not optimal for very large numbers or linked list-based constraints

# ⚡ Optimization / Pattern Used:
# Pattern: **Digit-by-digit addition with carry**
# - Traverse both lists simultaneously
# - Add corresponding digits and carry
# - Keep track of carry for the next node

# 🔑 Key Insight:
# Treat each list node like a digit place (units, tens, hundreds…)
# Handle edge cases: different list lengths and final carry

# 🧠 Why it works:
# - Mimics how we add numbers on paper, digit by digit with carry
# - Reversing order ensures we build the list in the correct forward manner from head to tail

# 📈 Time & Space Complexity:
# Time: O(max(m, n)) — where m and n are lengths of the input lists
# Space: O(max(m, n)) — result list size + carry

# 📝 My Takeaway:
# ✅ Classic linked list arithmetic problem
# ✅ Handling edge cases like uneven lengths and final carry is key
# ✅ Dummy head + current pointer = go-to trick for building new lists
