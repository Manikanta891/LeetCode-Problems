class Solution:
    def eraseOverlapIntervals(self, intervals ):
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        
        res = 0
        last_end_time = intervals[0][1]

        for i in range(1, n):
            start_time, end_time = intervals[i]
            if start_time < last_end_time:
                res += 1
            else:
                last_end_time = end_time

        return res
    

# 🚀 Problem Summary:
# Given: A list of intervals [start, end]
# Goal: Remove the **minimum number of intervals** so that the rest do not overlap
# Return: The number of intervals to remove

# 🧩 Brute Force Idea:
# Compare each interval with all others, remove the one that causes overlap
# Time: O(n^2) — check each pair
# Space: O(1)
# Not efficient for large input sizes

# ⚡ Optimization / Pattern Used:
# Pattern: Greedy — sort by end time
# Idea:
#   - Sort intervals by end time (to keep intervals that end earlier)
#   - Start with the first interval, keep track of its end time
#   - For each next interval:
#       - If its start time < last_end_time → there's an overlap → remove (count it)
#       - Else → accept this interval and update last_end_time
# Why this works? → Ending earlier gives more room for future intervals → maximizes non-overlapping count

# 🔑 Key Insight:
# Sorting by end time is the key greedy step
# By always choosing the interval that ends the earliest, we leave space for others

# 🧠 Why it works:
# This is the **activity selection problem** from greedy algorithms
# The optimal way to select maximum non-overlapping intervals is by choosing intervals that end first

# 📈 Time & Space Complexity:
# Time: O(n log n) — for sorting the intervals
# Space: O(1) — no extra data structures (just a counter and pointer)

# 📝 My Takeaway:
# This is a golden greedy pattern — sort by end, take what doesn’t conflict
# Always think of “what local choice leads to global optimal?”
# It’s also a trick to remember for interval questions in interviews
