# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         right = 0
#         s1_len = len(s1)
#         s2_len = len(s2)
        
#         if s1_len > s2_len:
#             return False

#         s1_sorted = sorted(s1)

#         while right < s2_len:
#             window = s2[right:right + s1_len]
#             if sorted(window) == s1_sorted:
#                 return True
#             right += 1

#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
    
# 🚀 Problem Summary:
# Given: Two strings s1 and s2
# Goal: Check if any permutation of s1 exists as a substring in s2

# 🧩 Brute Force Idea:
# Slide a window of length `len(s1)` across `s2`
# For each window, check if it's a permutation of `s1`
# Use sorted() or Counter to compare
# Time: O(n·logn), Space: O(n)

# ⚡ Optimization / Pattern Used:
# Pattern: Sliding Window + Frequency Comparison
# Keep character count arrays for:
# → s1 (fixed)
# → s2 window (updated as window slides)
# Track how many matching char frequencies there are

# 🔑 Key Insight:
# You only need to compare **26 characters**
# → Use a `matches` counter to track how many indices match
# → Only update what changed as window slides

# 🧠 Why it works:
# Each time a char enters or exits the window,
# we check if that change increases or decreases matches
# When `matches == 26`, all counts match ⇒ valid permutation found

# 📈 Time & Space Complexity:
# Time: O(n) — every char is processed once
# Space: O(1) — fixed 26-length arrays

# 📝 My Takeaway:
# ✅ Excellent use of frequency count deltas instead of full array comparison
# ✅ `ord(char) - ord('a')` trick keeps it compact and fast
# ✅ This is a gold-standard pattern for “permutation-in-substring” problems
