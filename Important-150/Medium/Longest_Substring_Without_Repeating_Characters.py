class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        seen=set()
        for r in s:
            while r in seen:
                seen.remove(s[l])
                l+=1
            seen.add(r)
            res=max(len(seen),res)
        return res


#Bruete Force Solution
# name="qwerqqqwweweewqwertyuiopasdfghjklzxcvbnm"
# seen=set()
# count=0
# max_count=0
# for i in range(len(name)):
#     for j in range(i,len(name)):
#         if name[j] not in seen:
#             seen.add(name[j])
#             count+=1
#         else:
#             seen.clear()
#             break
#     if count>max_count:
#         max_count=count
#         result=name[i:j]
#     count=0
# print(max_count)
# print(result)


# 🚀 Problem Summary:
# Given: A string `s`
# Goal: Return the length of the longest substring without repeating characters

# 🧩 Brute Force Idea:
# Try every possible substring using two loops
# For each substring, use a set to check if it contains all unique characters
# Track the max length among all valid substrings
# Time: O(n^3) — two loops + checking for uniqueness with a set
# Space: O(k) for the set (k = length of substring)

# ⚡ Optimization / Pattern Used:
# Pattern: Sliding Window + Set
# Left and right pointers define the current window
# Move the right pointer and add characters to the set
# If duplicate found, shrink the window from the left until it's valid
# Why needed? → Avoids recomputation and drastically cuts down time complexity

# 🔑 Key Insight:
# Use a set to track characters in the current window
# If a duplicate appears, shrink the window from the left side
# Always maintain a window of unique characters

# 🧠 Why it works:
# The sliding window grows when characters are unique, and shrinks on duplicates
# Ensures every window considered is valid (no repeated characters)
# Efficiently explores the string in a single pass

# 📈 Time & Space Complexity:
# Time: O(n) — Each character is added and removed at most once
# Space: O(k) — k is the size of the character set (at most 26–128 depending on charset)

# 📝 My Takeaway:
# Sliding window is perfect when the problem involves substrings or subarrays with conditions
# This technique avoids brute-force overhead and works great when you need to maintain a window with some invariant (like all unique chars)



