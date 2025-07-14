class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
    
    
# 🚀 Problem Summary:
# Given: List of prices where `prices[i]` is the stock price on day i
# Goal: Find the max profit you can make from **one** buy-sell transaction
#       (Buy before you sell!)

# 🧩 Brute Force Idea:
# Try every pair (i, j) where i < j → check profit `prices[j] - prices[i]`
# Time: O(n^2)
# Space: O(1)
# Way too slow for big inputs

# ⚡ Optimization / Pattern Used:
# Pattern: Sliding Window (Two Pointers)
# Use two pointers:
#   - `l` = buy day
#   - `r` = current day to sell
# If `prices[r] > prices[l]`, calculate profit
# Else, update `l = r` (buy at lower price)

# 🔑 Key Insight:
# You only need to track:
#   - the **lowest price so far** (left pointer)
#   - the **max profit** if selling today (right pointer)

# 🧠 Why it works:
# You iterate once, adjusting your "buy day" as needed
# Always check best profit between `prices[r] - prices[l]`

# 📈 Time & Space Complexity:
# Time: O(n) — single pass
# Space: O(1) — constant memory

# 📝 My Takeaway:
# 🔥 This is a **foundational greedy + windowing pattern**
# ✅ Remember: Reset the buy pointer if you find a lower price
# Also useful for: max subarray, min window, rainwater trap, etc.
