class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# 🚀 Problem Summary:
# Given: A string `s` and an integer `k`
# Goal: Return the length of the **longest substring** where you can replace ≤ k characters to make all characters the same

# 🧩 Brute Force Idea:
# Check all substrings, for each:
# → Count char frequencies
# → Replace others to match max frequency char
# Time: O(n^2 * 26), Space: O(26) for each substring
# Too slow for long strings

# ⚡ Optimization / Pattern Used:
# Pattern: Sliding Window + Frequency Count
# Key idea:
# → In window [l, r], we can convert up to `k` non-majority characters
# → We track the most frequent character (`maxf`) in current window
# → If (window size - maxf) > k, shrink the window from left

# 🔑 Key Insight:
# We don’t care which char dominates — just that we can replace `<= k` others
# So always keep the window if replacements needed are ≤ k

# 🧠 Why it works:
# If (r - l + 1) - maxf > k → we’ve exceeded our allowed replacements
# → So move `l` forward to shrink window
# At every step, store the longest valid window size in `res`

# 📈 Time & Space Complexity:
# Time: O(n) — each char is processed at most twice (enter & leave window)
# Space: O(26) = O(1) — only 26 letters, hashmap is constant size

# 📝 My Takeaway:
# ✅ This is a **perfect template** for fixed-char replacements in substrings
# ✅ Use `(window size - max freq char)` to know how many replacements needed
# ✅ Greedy maxf tracking keeps the logic fast and tight
