class Solution:
    def trap(self, h):
        l=0
        r=len(h)-1
        lmax=h[l]
        rmax=h[r]
        res=0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,h[l])
                res+=lmax-h[l]
            else:
                r-=1
                rmax=max(rmax,h[r])
                res+=rmax-h[r]
        return res

# This is the two pointers approach lets think me and my friend Venu is doing same
# But here instead we are doing in a different way

# We are in between hills me at starting venu is at end point
# Now we contact with each other i store the lmax of my side 
# Venu store rmax of his side 
# Now if mine lmax is less than venu rmax i move a head and count the water can fill
# in the empty place 
# {Because no matter how much i move venu sides hills can be hold that water}

# If venu side rmax is less than me then he will move towards my side 
# {Because no matter how he will move my sides hills can be hold that water}

# Like wise we calculate the height of water we can store

#Brute Force Approach 

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#         n = len(height)
#         res = 0

#         for i in range(n):
#             leftMax = rightMax = height[i]

#             for j in range(i):
#                 leftMax = max(leftMax, height[j])
#             for j in range(i + 1, n):
#                 rightMax = max(rightMax, height[j])
                
#             res += min(leftMax, rightMax) - height[i]
#         return res

# Index | Height | LeftMax | RightMax | Min(LeftMax, RightMax) | Water Stored
# ------|--------|---------|----------|-------------------------|--------------
#   0   |   0    |    0    |     3    |            0            |      0
#   1   |   2    |    2    |     3    |            2            |      0
#   2   |   0    |    2    |     3    |            2            |      2
#   3   |   3    |    3    |     3    |            3            |      0
#   4   |   1    |    3    |     3    |            3            |      2
#   5   |   0    |    3    |     3    |            3            |      3
#   6   |   1    |    3    |     3    |            3            |      2
#   7   |   3    |    3    |     3    |            3            |      0
#   8   |   2    |    3    |     2    |            2            |      0
#   9   |   1    |    3    |     1    |            1            |      0

# 🚀 Problem Summary:
# Given: A list of integers representing elevation map `height`
# Goal: Compute how much water can be trapped between the bars after raining

# 🧩 Brute Force Idea:
# For each bar at index `i`, find:
#   - max height on the left (0 to i)
#   - max height on the right (i to n-1)
# Water trapped = min(left_max, right_max) - height[i]
# Repeat for each bar
# Time: O(n^2) — two nested loops for each bar
# Space: O(1)

# ⚡ Optimization / Pattern Used:
# Pattern: Two Pointers + Greedy + Preprocessing (Optional prefix array in some versions)
# Left pointer (you), right pointer (Venu) start from opposite ends
# lmax stores max height seen from left; rmax from right
# - If lmax < rmax, move left forward and trap water based on lmax
# - Else move right backward and trap water based on rmax
# Why needed? → Avoids repeated max calculations for each index

# 🔑 Key Insight:
# At any point, the water trapped is determined by the shorter of the two sides (left or right)
# So we move the pointer with the smaller max value inward
# Because that side **cannot** trap more water even if we wait — we need the opposite side to grow

# 🧠 Why it works:
# Each position contributes to trapped water based on the "minimum of max heights from both sides"
# Using two pointers and updating max as we move ensures only one pass (O(n)) is required

# 📈 Time & Space Complexity:
# Time: O(n) — single traversal with two pointers
# Space: O(1) — only variables used (no extra arrays)

# 📝 My Takeaway:
# This problem trains deep thinking on **left-right symmetry** and dynamic condition handling
# The two-pointer trick here isn't just a space saver, it's also a brilliant logic simplifier
# Visualizing yourself and Venu working from both ends is the best intuition booster ever
