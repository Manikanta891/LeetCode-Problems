# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         length=len(nums)
#         i=0
#         while i<length:
#             if nums[i]==val:
#                 nums.pop(i)
#                 length-=1
#                 i-=1
#             i+=1
#         return len(nums)


#Actually question is different then what i think i thought of returning the len of remainig array 
#But when i return the remaing array that will consider nums position of remaing array 
#So i need to do removing the element anyway
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for next valid spot
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# 🚀 Problem Summary:
# Given: An array `nums` and an integer `val`
# Goal: Remove all instances of `val` in-place and return the new length `k` of the array
#       The first `k` elements of `nums` should be the remaining valid elements

# 🧩 Brute Force Idea:
# Use `pop()` to remove each occurrence of `val`
# But `pop(i)` inside a loop causes O(n) shifting for each removal
# Time: O(n^2) in worst case
# Space: O(1)
# Not efficient for large arrays

# ⚡ Optimization / Pattern Used:
# Pattern: Two Pointers (read and write index)
# → Use pointer `k` to track the next valid write position
# → Scan from `i = 0` to `n-1`
#     - If nums[i] != val, write nums[i] to nums[k] and increment `k`
# → At the end, `k` is the length of the updated array
# Why needed? → Efficient in-place update, no shifting or popping

# 🔑 Key Insight:
# You don’t need to return the modified array — just ensure first `k` elements are valid
# It's okay to overwrite from the beginning as long as order of valid elements is preserved

# 🧠 Why it works:
# This approach guarantees that only non-`val` elements are kept at the beginning
# Remaining values beyond index `k` are ignored as per problem statement

# 📈 Time & Space Complexity:
# Time: O(n) — single pass through array
# Space: O(1) — no extra memory used

# 📝 My Takeaway:
# Simple, powerful use of two pointers
# Great pattern for:
#   - Remove Duplicates
#   - Move Zeros
#   - Partition Arrays
# Learn this once, apply it everywhere
