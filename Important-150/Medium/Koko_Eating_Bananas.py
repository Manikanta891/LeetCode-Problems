import math
class Solution:
    def minEatingSpeed(self, piles):
        left=1
        right=max(piles)
        result=right
        while left<=right:
            k=(left+right)//2
            time=sum(math.ceil(p/k) for p in piles)
            
            if time<=h:
                result=k
                right=k-1
            else:
                left=k+1
        return result




# Bruete Force approach
# import math
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         if not piles :
#             return 0
#         min_hours=max(piles)
#         for i in range(1,max(piles)+1):
#             time=0
#             for j in range(len(piles)):
#                 time+=math.ceil(piles[j]/i)
#             if h>=time:
#                 return i
#         return min_hours



# 🚀 Problem Summary:
# Given: 
#   - `piles`: list of integers where piles[i] is the number of bananas in the i-th pile
#   - `h`: total number of hours Koko has to eat all bananas
# Goal: Find the minimum integer speed `k` (bananas/hour) such that she can eat all bananas within `h` hours

# 🧩 Brute Force Idea:
# Try every eating speed `k` from 1 to max(piles)
# For each `k`, calculate total hours needed: sum(ceil(pile / k))
# Return the smallest `k` for which total hours <= `h`
# Time: O(max(pile) * n) — very slow when pile values are large
# Space: O(1)

# ⚡ Optimization / Pattern Used:
# Pattern: Binary Search on Answer
# Search range: from `left = 1` to `right = max(piles)`
# For a mid value `k`, check if Koko can eat all bananas in `h` hours using:
#     time = sum(ceil(pile / k) for pile in piles)
# Adjust search bounds:
#     - If time <= h: valid speed → try smaller (right = k - 1)
#     - If time > h: not valid → try faster (left = k + 1)
# Why needed? → Reduces linear search on large range down to log scale

# 🔑 Key Insight:
# We're not searching the input — we're searching the **solution space** (valid values of `k`)
# This is a classic use of binary search where the answer is monotonic (smaller `k` → more time)

# 🧠 Why it works:
# The total time is a non-increasing function of speed `k`
# So we can apply binary search to find the smallest `k` where time <= h

# 📈 Time & Space Complexity:
# Time: O(n * log m) — n = number of piles, m = max pile size (search space)
# Space: O(1)

# 📝 My Takeaway:
# This is a great example of binary search beyond arrays — directly on answer space
# Whenever brute force loops over a large range and you have a "yes/no" condition → try binary search
# `math.ceil` is a handy trick here to avoid float issues
