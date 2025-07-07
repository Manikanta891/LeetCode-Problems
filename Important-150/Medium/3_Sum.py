# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result=set()
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if(nums[i]+nums[j]+nums[k]==0) and tuple([nums[i],nums[j],nums[k]]) not in result:
#                         result.add(tuple(sorted([nums[i],nums[j],nums[k]])))
#         return [list(triplet) for triplet in result]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate `i` values

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


# 🚀 Problem Summary:
# Given: An integer array `nums`
# Goal: Find all unique triplets [a, b, c] such that a + b + c = 0
# Triplets must be in non-descending order and no duplicates allowed in output

# 🧩 Brute Force Idea:
# Use 3 nested loops to check all combinations
# Check if the sum is 0 and ensure no duplicates in result set
# Time: O(n^3) — very slow for large input
# Space: O(n) for set of unique triplets

# ⚡ Optimization / Pattern Used:
# Pattern: Sorting + Two Pointers
# Step 1: Sort the array
# Step 2: Fix the first element (`i`) and use two pointers (`left`, `right`) to find remaining pair
# - If sum == 0 → store triplet, skip duplicates
# - If sum < 0 → move left pointer (need bigger number)
# - If sum > 0 → move right pointer (need smaller number)
# Why needed? → Reduces O(n^3) to O(n^2) and handles duplicates elegantly

# 🔑 Key Insight:
# Sorting allows skipping duplicates easily
# Two pointers allow us to scan possible pairs in linear time

# 🧠 Why it works:
# Fixing one number and scanning the remaining array for two numbers that sum to the negative of it reduces the complexity
# By skipping duplicates after adding a triplet, we avoid repeated results

# 📈 Time & Space Complexity:
# Time: O(n^2) — outer loop + inner two-pointer scan
# Space: O(1) (ignoring output list) — no extra data structures needed

# 📝 My Takeaway:
# This problem is the classic gateway to mastering:
#   - Sorting + two pointer technique
#   - Duplicate handling in arrays
# It’s foundational for solving variants like:
#   - 3Sum Closest
#   - 4Sum
#   - k-Sum (generalized)
