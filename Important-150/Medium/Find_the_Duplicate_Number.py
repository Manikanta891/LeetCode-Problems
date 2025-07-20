class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     seen=set()
    #     i=len(nums)-1
    #     while i>=0:
    #         if nums[i] in seen:
    #             return nums[i]
    #         seen.add(nums[i])
    #         i-=1

    def findDuplicate(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)# already visited → duplicate
            else:
                nums[idx] *= -1       # mark as visited

# 🚀 Problem Summary:
# Given: A list of `n+1` integers where each integer is in range [1, n]
# Goal: Return any **duplicate number** present in the list

# 🧩 Brute Force Idea:
# - Use a `set()` to track seen elements
# - On re-seeing an element → return it
# Time: O(n), Space: O(n)

# ⚡ Optimization / Pattern Used:
# Pattern: **Index Marking (In-place Mutation)**
# - Each number maps to an index (num - 1)
# - If `nums[idx]` is negative → already visited → duplicate found
# - Else, mark it visited by negating

# 🔑 Key Insight:
# Since values are in [1, n], we can use them as indices
# Mutating the array in-place avoids extra space usage

# 🧠 Why it works:
# - Negative marking preserves information in-place
# - The first time we revisit a marked index, we’ve found a duplicate
# - This works **only** because all numbers are positive initially

# 📈 Time & Space Complexity:
# Time: O(n)
# Space: O(1) (in-place, no extra data structures)

# 📝 My Takeaway:
# ✅ Index-based value tricks are a **powerful space-saving technique**
# ✅ Must ensure that **mutation is allowed** (some interviewers may disallow it!)
# ✅ This pattern is super useful in variations: "missing number", "first positive", etc.
