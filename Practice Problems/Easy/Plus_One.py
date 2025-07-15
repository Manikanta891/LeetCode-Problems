# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         i=len(digits)-1
#         while 1 :
#             if digits[i]==9 and i>0:
#                 digits[i]=0
#                 i-=1
#             elif digits[i]==9 and i==0:
#                 digits[i]=0
#                 digits.insert(0,1)
#                 break
#             else:
#                 digits[i]+=1
#                 break
#         return digits
    
def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits  # all 9s case


# 🚀 Problem Summary:
# Given: A list `digits` representing a non-negative integer
# Goal: Add 1 to the number and return the resulting list of digits

# 🧩 Brute Force Idea:
# Convert the list to an integer, add 1, then convert back
# Problem: Can lead to overflow or type conversion issues on huge inputs
# Time: O(n), but memory isn't optimized

# ⚡ Optimization / Pattern Used:
# Pattern: Simulate manual addition (like how you’d add on paper)
# Start from the last digit
# → If digit is 9, set to 0 and carry over
# → If not 9, increment and exit

# 🔑 Key Insight:
# Carry only propagates if you keep seeing 9s
# Special case: if all digits are 9 (e.g., [9,9,9]) → becomes [1,0,0,0]

# 🧠 Why it works:
# It directly mimics how addition with carry works
# Mutates in place with edge case handling (inserting 1 at front)

# 📈 Time & Space Complexity:
# Time: O(n) — in worst case, all digits are 9
# Space: O(1) extra (excluding output list, modifies in place)

# 📝 My Takeaway:
# ✅ Simulating real-world math logic is often better than converting types
# ✅ Carefully handle edge cases like leading carry
# 💡 Using a loop with breaks lets you skip unnecessary checks
