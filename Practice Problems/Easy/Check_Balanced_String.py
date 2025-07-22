class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0

        for i in range(len(num)):
            if i % 2 == 0:
                even_sum += int(num[i])
            else:
                odd_sum += int(num[i])

        return even_sum == odd_sum



# 🚀 Problem Summary:
# Given: A numeric string `num`.
# Goal: Determine if the number is **balanced**, i.e., the sum of digits at even indices is equal to the sum of digits at odd indices.

# 🧩 Brute Force Idea:
# Traverse the string character by character.
# Keep two sums — one for even-indexed digits and one for odd-indexed digits (based on 0-based indexing).
# Compare the sums at the end.
# Time Complexity: O(n)
# Space Complexity: O(1)

# ⚡ Optimization / Pattern Used:
# No advanced optimization needed since the brute-force itself is optimal (O(n) time, O(1) space).
# Pattern: Basic index-based traversal and conditional accumulation.

# 🔑 Key Insight:
# Since the positions are known, we can distinguish even and odd indices while looping through the string.
# Using 0-based indexing, index % 2 == 0 implies **even-indexed digit**.

# Edge Cases:
# - If the string is empty -> return True
# - If there's only one digit -> return True (nothing to compare, so it's trivially balanced)

# 🧠 Why it works:
# It directly tracks the parity of index and sums accordingly.
# Since all characters are digits, we safely convert to integers.

# 📈 Time & Space Complexity:
# Time: O(n), where n is the length of the input string
# Space: O(1), uses only constant space for tracking sums

# 📝 My Takeaway:
# This was a great example of solving a problem by simply tracking pattern using index parity.
# Reinforced how sometimes brute force is already optimal when there is no better trade-off.

